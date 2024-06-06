import json
import csv
from math import ceil
import re
from collections import OrderedDict
from os import makedirs
from collections import defaultdict

outDir = 'scrapedJSON/ref/wildareas/'
makedirs(outDir, exist_ok = True)

encounterTableFile = 'scrapedJSON/ref/nestedEncounterTable.json'
with open(encounterTableFile, mode = 'r') as e:
    storyAreas = json.load(e)

wildAreas = storyAreas['Main Story']
wildAreas.update(storyAreas['Postgame Locations'])

# Need to step into each as far down until you hit a list...?
# need to fix this???

def unnest(d, keys=[]):
    result = []
    for k, v in d.items():
        if isinstance(v, dict):
            result.extend(unnest(v, keys + [k]))
        else:
            result.append(tuple(keys + [k, v]))
    return result

flattened_encounters = []
for area, tables in wildAreas.items():
    aa = unnest(tables, [area])
    [flattened_encounters.append(a) for a in aa]

pkmn_first_flattened = []
for f in flattened_encounters:
    ff = list(f)
    pkmn = ff[-2]
    ff.pop(-2)
    pkmn_first_flattened.append(tuple([pkmn]+ff))

def update_dict(d,l):
    if not isinstance(l[1], list):
        d[l[0]] = update_dict(d[l[0]], l[1:])
    else:
        d[l[0]] = l[1]
    return d
        
nested_dict = lambda: defaultdict(nested_dict)

def_dict = nested_dict()
for row in pkmn_first_flattened:
    def_dict = update_dict(def_dict, row)
out_dict = dict(def_dict)
with open('./scrapedJSON/ref/pokemonEncounters.json', mode = 'w') as outFile:
    outFile.write(json.dumps(out_dict, indent = 4))
tmp = 1