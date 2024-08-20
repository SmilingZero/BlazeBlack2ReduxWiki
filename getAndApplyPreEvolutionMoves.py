from genericpath import isfile
import os
import tqdm
import json
import networkx as nx
from itertools import groupby

def getint(name):
    basename = name.partition('.')
    return int(basename[0])


pkmnDir = './scrapedJSON/pokemon/'
listOfPokemonFiles = [f for f in os.listdir(pkmnDir) if f.endswith('.json')]
listOfPokemonFiles.sort(key=getint)

#####
# Scrape JSON
# Add Nodes
#####
pkmn_data = []
name_overrides = ['Deoxys', 'Wormadam', 'Giratina', 'Shaymin', 'Basculin', 'Darmanitan', 'Tornadus', 'Thundurus', 'Landorus', 'Keldeo', 'Meloetta']
evolution_graph = nx.DiGraph()
for ind, jsonFile in enumerate(tqdm.tqdm(listOfPokemonFiles)):
    with open(pkmnDir+jsonFile) as pkmnFile:
        main_form = json.load(pkmnFile)[0]
        for o in name_overrides:
            if o in main_form['Name']:
                main_form['Name'] = o
        pkmn_data.append(main_form)
        evolution_graph.add_node(main_form['Name'])
        
#####
# Add Edges
#####
for ind, pkmn in enumerate(tqdm.tqdm(pkmn_data)):
    main_form = pkmn
    if "Evolutions" not in main_form.keys():
        continue
    if len(main_form["Evolutions"]) == 0:
        continue
    evol_dest = [ e["To"] for e in main_form["Evolutions"]]
    for ii, evol in enumerate(evol_dest):
        for o in name_overrides:
            if o in evol:
                evol_dest[ii] = o
    for evol in evol_dest:
       evolution_graph.add_edge(main_form['Name'], evol)

'''
Get all weakly connected components (corresponds to evolution branches) and walk the edges to determine if there are moves missing in the jump
'''
evo_branches = [evolution_graph.subgraph(c).copy() for c in nx.weakly_connected_components(evolution_graph)]
def get_move_list(p_list):
    move_keys = ["Tutor Moves", "Level Up Moves", "TM Moves"]
    move_list = []
    for p in p_list:
        moves_to_add = []
        for k in move_keys:
            if k not in p.keys():
                continue
            if len(p[k]) == 0:
                continue
            match k:
                case "Tutor Moves":
                    tmp = [('Tutor', m) for m in p[k]]
                case "Level Up Moves":
                    tmp = [('Lvl {n}'.format(n = m['Level']), m['Move']) for m in p[k]]
                case "TM Moves":
                    tmp = [(m['Machine'], m['Name']) for m in p[k]]
                case _:
                    ValueError
            moves_to_add.extend(tmp)
        collapse_moves_to_add = [(p['Name'], ' / '.join([g[0] for g in group]), k) for k, group in groupby(sorted(moves_to_add, key=lambda x:x[1]), lambda x: x[1])]
        [move_list.append(m) for m in collapse_moves_to_add]
    return move_list


pre_evo_dict = {} # note will need to remove non-unique entries {number: list of tuples}
completed_edges = {}
for ind, evo_branch in enumerate(tqdm.tqdm(evo_branches)):
    start_node = [n for n,d in evo_branch.in_degree if d == 0][0]
    end_nodes = [n for n,d in evo_branch.out_degree if d == 0]
    for final_evo in end_nodes:
        path = [p for p in nx.all_simple_edge_paths(evo_branch, start_node, final_evo)][0]
        for i in range(0, len(path)):
            # get all edges between this and "behind it" in the path
            edges_considered = path[0:i+1]
            #create list of unique nodes --> must keep evo order in tact
            all_nodes = [e for l in edges_considered for e in l]
            all_nodes = sorted(set(all_nodes), key=all_nodes.index)
            all_moves_by_node = [get_move_list([p for p in pkmn_data if p['Name'] == v]) for v in all_nodes]
            # remove redundant moves from earlier nodes (e.g. if x->y->z and x/y learn the same move, remove it from the "x" list)
            unique_moves = all_moves_by_node
            for j in range(0, len(all_moves_by_node)-1):
                this_node = all_moves_by_node[j]
                this_move_names = set([m[2] for m in this_node])
                next_nodes = [e for l in all_moves_by_node[j+1:] for e in l]
                next_move_names = set([m[2] for m in next_nodes])
                unique_this_move_names = this_move_names - next_move_names
                unique_moves[j] = [m for m in this_node if m[2] in unique_this_move_names]
            pre_node_moves = [e for l in unique_moves[:-1] for e in l]

            final_evo_number =  [p for p in pkmn_data if p['Name'] == all_nodes[-1]][0]['Number']
            if len(pre_node_moves) == 0:
                continue
            if final_evo_number in pre_evo_dict.keys() and len(pre_evo_dict[final_evo_number]) > 0 and pre_evo_dict[final_evo_number] != pre_node_moves:
                    raise RuntimeError
            pre_evo_dict[final_evo_number] = pre_node_moves            
'''
Add information back to target JSON
'''
for pk_num,lost_moves in pre_evo_dict.items():
    filename = f"{pk_num:03d}.json"
    with open(pkmnDir+filename, 'r') as pkmnFile:
        current_json = json.load(pkmnFile)
    current_json[0]['Pre-Evolution Moves'] = lost_moves
    with open(pkmnDir+filename, 'w') as pkmnFile:
        pkmnFile.write(json.dumps(current_json))
    stop = 1