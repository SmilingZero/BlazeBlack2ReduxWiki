import json
import csv
from math import ceil
import re
from collections import OrderedDict
from os import makedirs
import encounterTableWriter

outDir = 'docs/wildareas/'
makedirs(outDir, exist_ok = True)

pageList = 'tmpWildAreaList.txt'

encounterTableFile = 'scrapedJSON/ref/nestedEncounterTable.json'
with open(encounterTableFile, mode = 'r') as e:
    wildAreas = json.load(e)



areaOrder = [['Aspertia City', 'Route 19', 'Floccesy Ranch', 'Route 20',\
              'Floccesy Ranch', 'Virbank City', 'Virbank Complex - Outside','Virbank Complex - Inside', \
              'Castelia City Gardens', 'Castelia Sewers', 'Relic Passage', 'Route 4',\
              'Desert Resort', 'Relic Castle', 'Route 5', 'Route 16', 'Lostlorn Forest', \
              'Driftveil Drawbridge, Charizard Bridge', 'Route 6', 'Clay Tunnel', 'Mistralton Cave',\
              'Chargestone Cave', 'Route 7', 'Celestial Tower', 'Reversal Mountain', 'Strange House',\
              'Undella Town', 'Undella Bay', 'Route 14', 'Abundant Shrine', 'Seaside Cave', 'Route 13',\
              'Route 12', 'Village Bridge', 'Route 11', 'Route 9', 'Route 21', 'Humilau City', 'Route 22', \
              'Giants Chasm', 'Route 23', 'Victory Road'], ['Route 8, Moor of Icirrus', 'Icirrus City', 'Dragonspiral Tower',\
                'Twist Mountain', 'Underground Ruins', 'Marvellous Bridge', 'Route 15',\
                'Pinwheel Forest - Inside', 'Pinwheel Forest - Outside', 'Route 3', 'Wellspring Cave',\
                'Striation City', 'Dreamyard', 'Route 2', 'Route 1', 'Route 17', 'Route 18', 'P2 Laboratory',\
                'The Nature Preserve']]



listString = '- Wild Areas:\n  - Specific Areas:\n'
linkDict = {}

for ind,(partOfGame,areas) in enumerate(wildAreas.items()):
    for area in areaOrder[ind]:
        filename = '{place}.md'.format(place = area.replace(' ', '_'))
        thisArea = areas[area]
        pageString = encounterTableWriter.getEncounterPage(area, thisArea)
        with open(outDir+filename, mode = 'w') as f:
            f.write(pageString)
        listString += '    - {place}: wildareas/{filename}\n'.format(place = area, filename = filename)
        linkDict[area] = filename

with open(pageList, mode = 'w') as f:
    f.write(listString)

with open('locationLinkDict.json', mode = 'w') as f:
    f.write(json.dumps(linkDict))