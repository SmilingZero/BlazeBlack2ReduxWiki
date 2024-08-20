import json
import csv
from math import ceil
import re
from collections import OrderedDict
from os import makedirs

image_base_link = '../../img/animated/'
pokemon_base_link = '../../pokemons/'

# methodList = ['Grass, Normal', 'Grass, Doubles','Grass, Shaking Spots' \
#               'Fish, Normal','Fish, Dark Spot','Surf, Normal','Surf, Dark Spot',\
#               'Cave, Normal', 'Cave, Dust Cloud', 'Cave, Main, Dust Cloud','Cave, Dark, Dust Cloud', 'Sand, Normal',\
#               'Bridge', 'Floor','Sewer', 'Rooms', 'Hidden Grottos', 'Static', 'Special']
# note need to reorg the encounter file so the subfields are in some kind ogf order???

pokemonImageLookup = './data/speciesImageLookup.json'
with open(pokemonImageLookup, 'r') as f:
    speciesImageLookup = json.load(f)

def getIsEncounterTable(testDict):
    # An encounter table is 2 layers of dicts Encounter Method -> Pokemon -> List of Data
    def max_depth(d):
        if isinstance(d, dict):
            return 1 + max((max_depth(value) for value in d.values()), default=0)
        return 0
    if(max_depth(testDict)==2):
        return True
    else:
        return False
    

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

def getEncounterRows(numMonCol,encounter):
    numMons = sum([len(v) for k,v in encounter[1].items()])
    numRows = ceil(numMons/numMonCol)
    numEntries = numRows*(numMonCol + 1)
    content = ['&nbsp;']*numEntries
    monIndices = [i for i in range(0, numEntries) if i % (numMonCol+1)]
    content[0] = encounter[0]
    contentCells = []
    for mon, entries in encounter[1].items():
        for entry in entries:
            e = (mon, entry)
            contentCells.append(getEncounterCell(e))
    # contentCells = [getEncounterCell(e) for e in list(encounter[1].items())]
    all_includes = list(set([c[1] for c in contentCells]))
    inclStr = '\n'.join(all_includes)
    cells = [c[0] for c in contentCells]
    for ind,c in enumerate(cells):
        cInd = monIndices[ind]
        content[cInd] = c
    rows = [
        '| ' +' | '.join([content[i] for i in range((r)*(numMonCol+1), (r+1)*(numMonCol+1))]) + ' |'
            for r in range(numRows)]
    rowStr = '\n'.join(rows)+'\n'
    return rowStr, inclStr

def generateEncounterTableMarkdown(encounterTable): 
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


def getEncounterMethodCell_HTML(m,r):
    #eventually adapt to add image and formatting
    cell_string = f"<td rowspan=\"{r}\" style=\"vertical-align: middle; word-wrap: break-word; text-align: center;\">{m}</td>"
    return cell_string

def getEncounterCell_HTML(encounter):
    pkmn = encounter[0]
    species, form = getSpecies(pkmn)
    thisMonImages = speciesImageLookup[species]
    thisMonIm = thisMonImages[form]
    imID = re.findall('(.+).gif', thisMonIm)[0]
    threeDigitNum = "{0:03}".format(thisMonImages['NatDexNum'])
    imageLink = image_base_link + thisMonIm
    imageLinkText = "<img src=\"{i}\">".format(i = imageLink)
    pkmnLinkText = "<a href=\"{hyperlink}\">{link_text}</a>".format(link_text = pkmn, hyperlink = pokemon_base_link + threeDigitNum)
    level = encounter[1]['Level']
    perc = round(encounter[1]['Spawn Percent'], 2)
    cellstr = "<td style=\"text-align: center; vertical-align: bottom;\"> {img} <br> {link} <br> Lv: {lvl} <br> {percent}% </td>"\
        .format(\
            img = imageLinkText, 
            link = pkmnLinkText,
            lvl = level,
            percent = perc
        )
    return cellstr

def getEncounterCells_HTML(encounters):
    encounterCells = []
    for mon, entries in encounters.items():
        for entry in entries:
            e = (mon, entry)
            encounterCells.append(getEncounterCell_HTML(e))
    return encounterCells


def getEncounterRowStringHTML(numMonCol, encounterTableEntry):
    encounterMethod = encounterTableEntry[0]
    encounterData = encounterTableEntry[1]
    numMons = sum([len(v) for k,v in encounterData.items()])
    numRows = ceil(numMons/numMonCol)
    encounterMethodCell = getEncounterMethodCell_HTML(encounterMethod, numRows)
    encounterCells = getEncounterCells_HTML(encounterData)
    encounterCells.extend(["<td></td>" for i in range(numMonCol)])
    encounterRowContent = [''.join(encounterCells[numMonCol*i : (i+1)*numMonCol]) for i in range(numRows)]
    encounterRowContent[0] = encounterMethodCell + encounterRowContent[0]
    html_rows = ["<tr>{s}</tr>".format(s = row) for row in encounterRowContent]
    return '\n'.join(html_rows)

def getKeyValue(k):
    match k:
        case "Grass":
            return 0
        case "Sand":
            return 0
        case "Dark Grass (Doubles)":
            return 1
        case "Shaking Grass":
            return 2
        case "Swamps":
            return 3
        case "Sewer":
            return 4
        case "Cave":
            return 5
        case "Dust Cloud":
            return 6
        case "Surf":
            return 10
        case "Surf, Rippling Water":
            return 11
        case "Fish":
            return 20
        case "Fish, Rippling Water":
            return 21
    if 'Sand' in k or 'Floor' in k or 'Shadows' in k or 'Room' in k:
        return 0
    if 'Hidden Grotto' in k:
        return 100
    if 'Special Event' in k:
        return 200
    if 'Event Encounter' in k:
        return 200
    if 'Static Encounter' in k:
        return 130
    if 'Special Gifts' in k:
        return 140
    return 0

def sortEncounterKeys(k):
    sorted_k = sorted(list(k), key=lambda x : getKeyValue(x))
    return sorted_k


def generateEncounterTableHTML(encounterTable):
    sorted_keys = sortEncounterKeys(encounterTable.keys())
    numMonCol = 5
    table_rows = []
    table_rows.append(f"<tr><th colspan=\"1\">Encounter Method</th><th colspan=\"{numMonCol}\" style = \"text-align: center;\">Available Pokémon</th></tr>")
    table_rows.extend([getEncounterRowStringHTML(numMonCol, (k, encounterTable[k])) for k in sorted_keys])
    table_body = '\n'.join(table_rows)
    table_string = '<table>{content}</table>'.format(content = table_body)

    return table_string

def generateSubareaStringMarkdown(subareas):
    subareaStrings = ['']*len(subareas)
    subareaIncls = ['']*len(subareas)
    for ind, (area, encounters) in enumerate(subareas.items()):
        contentString, incl = generateEncounterTableMarkdown(encounters)
        subareaStrings[ind] = '## {place}\n\n'.format(place=area)+contentString
        subareaIncls[ind] = incl
    totStr = '\n'.join(subareaStrings)+'\n'
    totIncl = '\n'.join(subareaIncls)+'\n'
    return totStr, totIncl

def generateSubareaString_HTML(subareas):
    subareaStrings = ['']*len(subareas)
    for ind, (area, encounters) in enumerate(subareas.items()):
        contentString= generateEncounterTableHTML(encounters)
        subareaStrings[ind] = '## {place}\n\n'.format(place=area)+contentString
    totStr = '\n'.join(subareaStrings)+'\n'
    return totStr

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
    inclStr = '[{num}]: ../img/animated/{imStr}\n[{name}]: ../../pokemons/{natNum}/'\
        .format(num=imID, imStr =thisMonIm, name=mon[0], natNum=threeDigitNum)
    return (cellStr, inclStr)


def getEncounterPage(area, thisArea):
    pageString = '# {place}\n\n'.format(place=area)
    
    
    if getIsEncounterTable(thisArea):
        contentString = generateEncounterTableHTML(thisArea)
    else:
        contentString = generateSubareaString_HTML(thisArea)
    # incl = "\n".join(list(OrderedDict.fromkeys(incl.split("\n"))))
    # pageString+=contentString+'\n\n'+incl
    pageString = contentString
    return pageString

