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
for k,v in wildAreas.items():
    with open(outDir+f"{k}.json", mode = 'w') as outFile:
        outFile.write(json.dumps({k:v}, indent=4))

        