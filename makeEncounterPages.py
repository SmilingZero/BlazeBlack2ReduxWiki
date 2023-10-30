import json
import csv
from math import ceil
import re
from collections import OrderedDict
from os import makedirs

outDir = 'docs/wildareas/'
makedirs(outDir, exist_ok = True)

pageList = 'tmpWildAreaList.txt'
encounterTableFile = 'scrapedJSON/ref/nestedEncounterTable.json'
with open(encounterTableFile, mode = 'r') as e:
    wildAreas = json.load(e)

pokemonImageLookup = './data/speciesImageLookup.json'
with open(pokemonImageLookup, 'r') as f:
    speciesImageLookup = json.load(f)

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

def getIsEncounterTable(testDict):
    # An encounter table is 3 layers deep Type -> Mon -> Data
    def max_depth(d):
        if isinstance(d, dict):
            return 1 + max((max_depth(value) for value in d.values()), default=0)
        return 0
    if(max_depth(testDict)==3):
        return True
    else:
        return False

# methodList = ['Grass, Normal', 'Grass, Doubles','Grass, Shaking Spots' \
#               'Fish, Normal','Fish, Dark Spot','Surf, Normal','Surf, Dark Spot',\
#               'Cave, Normal', 'Cave, Dust Cloud', 'Cave, Main, Dust Cloud','Cave, Dark, Dust Cloud', 'Sand, Normal',\
#               'Bridge', 'Floor','Sewer', 'Rooms', 'Hidden Grottos', 'Static', 'Special']
# note need to reorg the encounter file so the subfields are in some kind ogf order???
def getHeaderAndSeparator(heading):
    return '| ' +' | '.join(heading) + ' |\n' + '|: ' +' :|: '.join(['---']*len(heading)) + ' :|\n'

def getSpecies(mon):
    hyphenInd = mon.find('-')
    if('♂' in mon):
        form = 'base'
        species= 'nidoranu2642'
    elif '♀' in mon:
        form = 'base'
        species= 'nidoranu2640'
    else:
        if hyphenInd == -1:
            form = 'base'
            species = mon.lower().strip()
        else:
            form = mon[hyphenInd+1:].strip().lower()
            species = mon[:hyphenInd].strip().lower()
        species = "".join([ c if c.isalnum() else "" for c in species ])
    return species, form

def getEncounterCell(mon):
    species, form = getSpecies(mon[0])
    thisMonImages = speciesImageLookup[species]
    thisMonIm = thisMonImages[form]
    imID = re.findall('(.+).gif', thisMonIm)[0]
    threeDigitNum = "{0:03}".format(thisMonImages['NatDexNum'])
    cellStr = '![][{num}] <br> __[{name}]__ <br> __Lv:__ {lvl} <br> __{perc}%__'.format(num = imID, 
                                                                               name = mon[0], 
                                                                               lvl = mon[1]['Level'],
                                                                               perc = round(mon[1]['Spawn Percent'], 2))
    inclStr = '[{num}]: ../img/animated/{imStr}\n[{name}]: ../pokemons/{natNum}/'\
        .format(num=imID, imStr =thisMonIm, name=mon[0], natNum=threeDigitNum)
    return (cellStr, inclStr)


def getEncounterRows(numMonCol,encounter):
    numMons = len(encounter[1])
    numRows = ceil(numMons/numMonCol)
    numEntries = numRows*(numMonCol + 1)
    content = ['&nbsp;']*numEntries
    monIndices = [i for i in range(0, numEntries) if i % (numMonCol+1)]
    content[0] = encounter[0]
    contentCells = [getEncounterCell(e) for e in list(encounter[1].items())]
    inclStr = '\n'.join([c[1] for c in contentCells])
    cells = [c[0] for c in contentCells]
    for ind,c in enumerate(cells):
        cInd = monIndices[ind]
        content[cInd] = c
    rows = [
        '| ' +' | '.join([content[i] for i in range((r)*(numMonCol+1), (r+1)*(numMonCol+1))]) + ' |'
            for r in range(numRows)]
    rowStr = '\n'.join(rows)+'\n'
    return rowStr, inclStr

def generateEncounterTableString(encounterTable): 
    numMonCol = 5
    headers = ['&nbsp;']*(numMonCol+1)
    headers[0] = '__Encounter<br>Method__'
    headers[3] = '__Available__'
    headers[4] = '__Pokémon__'
    tableString = getHeaderAndSeparator(headers)
    rowList = [getEncounterRows(numMonCol,e) for e in encounterTable.items()]
    tableString+=''.join([r[0] for r in rowList])
    inclString = '\n'.join([r[1] for r in rowList])
    return tableString, inclString

def generateSubareaString(subareas):
    subareaStrings = ['']*len(subareas)
    subareaIncls = ['']*len(subareas)
    for ind, (area, encounters) in enumerate(subareas.items()):
        contentString, incl = generateEncounterTableString(encounters)
        subareaStrings[ind] = '## {place}\n\n'.format(place=area)+contentString
        subareaIncls[ind] = incl
    totStr = '\n'.join(subareaStrings)+'\n'
    totIncl = '\n'.join(subareaIncls)+'\n'
    return totStr, totIncl

listString = '- Wild Areas:\n  - Specific Areas:\n'
linkDict = {}

for ind,(partOfGame,areas) in enumerate(wildAreas.items()):
    for area in areaOrder[ind]:
        thisArea = areas[area]
        isEncounterTable = getIsEncounterTable(thisArea)
        pageString = '# {place}\n\n'.format(place=area)
        filename = '{place}.md'.format(place = area.replace(' ', '_'))
        if isEncounterTable:
            contentString, incl = generateEncounterTableString(thisArea)
        else:
            contentString, incl = generateSubareaString(thisArea)
        incl = "\n".join(list(OrderedDict.fromkeys(incl.split("\n"))))
        pageString+=contentString+'\n\n'+incl
        with open(outDir+filename, mode = 'w') as f:
            f.write(pageString)
        listString += '    - {place}: wildareas/{filename}\n'.format(place = area, filename = filename)
        linkDict[area] = filename

with open(pageList, mode = 'w') as f:
    f.write(listString)

with open('locationLinkDict.json', mode = 'w') as f:
    f.write(json.dumps(linkDict))