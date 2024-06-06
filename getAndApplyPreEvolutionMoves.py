from genericpath import isfile
import os
import tqdm
import json
import csv
import re
import networkx as nx

def getint(name):
    basename = name.partition('.')
    return int(basename[0])


pkmnDir = 'scrapedJSON/pokemon/'
listOfPokemonFiles = os.listdir(pkmnDir)
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
    for evol in evol_dest:
       evolution_graph.add_edge(main_form['Name'], evol)

'''
Get all weakly connected components (corresponds to evolution branches) and walk the edges to determine if there are moves missing in the jump
'''
evo_branches = [evolution_graph.subgraph(c).copy() for c in nx.weakly_connected_components(evolution_graph)]
def get_move_list(p):
    move_keys = ["Tutor Moves", "Level Up Moves", "TM Moves"]
    move_list = []
    for k in move_keys:
        if k not in p.keys():
            continue
        if len(p[k]) == 0:
            continue
        match k:
            case "Tutor Moves":
                moves_to_add = [(p['Name'], 'Tutor', m) for m in p[k]]
            case "Level Up Moves":
                moves_to_add = [(p['Name'], 'Lvl {n}'.format(n = m['Level']), m['Move']) for m in p[k]]
            case "TM Moves":
                moves_to_add = [(p['Name'], m['Machine'], m['Name']) for m in p[k]]
            case _:
                ValueError
        [move_list.append(m) for m in moves_to_add]
    return move_list


pre_evo_dict = {} # note will need to remove non-unique entries {number: list of tuples}
completed_edges = {}
for ind, evo_branch in enumerate(tqdm.tqdm(evo_branches)):
    if 'Hoppip' in evo_branch:
        stop = 1
    start_node = [n for n,d in evo_branch.in_degree if d == 0][0]
    end_nodes = [n for n,d in evo_branch.out_degree if d == 0]
    for final_evo in end_nodes:
        path = [p for p in nx.all_simple_edge_paths(evo_branch, start_node, final_evo)][0]
        tPreEvoMoves = []
        for edge in path:
            if edge in completed_edges.keys():
                [tPreEvoMoves.append(entry) for entry in completed_edges[edge]]
                continue
            pre_moves = get_move_list([p for p in pkmn_data if p['Name'] == edge[0]][0])
            post = [p for p in pkmn_data if p['Name'] == edge[1]][0]
            post_moves = get_move_list(post)
            pre_move_names = set([m[2] for m in pre_moves])
            post_move_names = set([m[2] for m in post_moves])
            moves_in_pre_not_in_post = pre_move_names - post_move_names
            lost_moves = [m for m in pre_moves if m[2] in moves_in_pre_not_in_post]
            this_lost_moves = lost_moves
            completed_edges[edge] = lost_moves
            [lost_moves.append(entry) for entry in tPreEvoMoves]
            [tPreEvoMoves.append(entry) for entry in this_lost_moves]
            if len(lost_moves) > 0:
                pre_evo_dict[post['Number']] = lost_moves

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