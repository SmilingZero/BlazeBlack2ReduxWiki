from genericpath import isfile
import os
import tqdm
import json
import networkx as nx
import pickle
from itertools import groupby
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
        evolution_graph.add_node(main_form['Name'], number=main_form['Number'])
        
#####
# Add Edges
#####
for ind, pkmn in enumerate(tqdm.tqdm(pkmn_data)):
    main_form = pkmn
    if "Evolutions" not in main_form.keys():
        continue
    if len(main_form["Evolutions"]) == 0:
        continue
    if main_form['Name'] == 'Shelmet':
        sfs = 1
    evol_dest = [ (e["To"], e['Method']) for e in main_form["Evolutions"]]
    # Shelmet has two ways to evolve
    evol_dest  = [(k, ' or '.join([g[1] for g in group])) for k, group in groupby(evol_dest, lambda x: x[0])]
    for evol in evol_dest:
       evolution_graph.add_edge(main_form['Name'], evol[0], label=evol[1])

'''
Get all weakly connected components (corresponds to evolution branches) and save to a pickle
'''
evo_branches = [evolution_graph.subgraph(c).copy() for c in nx.weakly_connected_components(evolution_graph)]
pickle.dump(evo_branches, open('scrapedJSON/ref/evo_branches.pickle', mode='wb'))
        