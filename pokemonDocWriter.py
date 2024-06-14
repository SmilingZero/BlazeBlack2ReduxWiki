import os
import json
import csv
from collections import OrderedDict
from difflib import SequenceMatcher

def unnest(d, keys=[]):
    result = []
    for k, v in d.items():
        if isinstance(v, dict):
            result.extend(unnest(v, keys + [k]))
        else:
            result.append(tuple(keys + [k, v]))
    return result

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
pokemonImageLookup = './data/speciesImageLookup.json'
with open(pokemonImageLookup, 'r') as f:
    speciesImageLookup = json.load(f)
pokemonIndexFile = './data/pokemonIndexList.csv'
with open(pokemonIndexFile, 'r', encoding='utf-8-sig') as indexFile:
    reader = csv.reader(indexFile)
    pokemonNumberMap = { row[2]: f"{int(row[1]):03}" for row in reader}
detailedMoveListFile = 'scrapedJSON/ref/moves_with_descriptions.json'
with open(detailedMoveListFile) as f:
    detailedMoveList = json.load(f)
pokemonEncounterLocations = 'scrapedJSON/ref/pokemonEncounters.json'
with open(pokemonEncounterLocations) as f:
    pokemonEncounters = json.load(f)
with open('locationLinkDict.json', mode = 'r') as f:
    locationLinks = json.load(f)

def getTypeIncludes():
    typesFolder = 'docs/img/type/'
    typeFiles = os.listdir(typesFolder)
    includeText = ''
    for i, fname in enumerate(typeFiles):
        typestring = fname.replace('.png', '')
        typeInclude = "[{type}]: ../img/type/{fid}\n".format(type=typestring, fid=fname)
        includeText += typeInclude
    return includeText

def getSpeciesTypeString(typeList):
    individualTypeStrings = ['![][{typename}]'.format(typename=s.lower()) for s in typeList]
    return '<br>'.join(individualTypeStrings)

def getTopLevelHeader(pkmnInformation):
    number = pkmnInformation['Number']
    natDexNumber = f"{number:03}"
    speciesName = pkmnInformation['Name']
    formMarkerInd = speciesName.find('-')
    if formMarkerInd != -1 and speciesName != 'Ho-Oh':
        speciesName = speciesName[:formMarkerInd].strip()
    
    headerText = "{number} - {speciesname}".format(number = natDexNumber, speciesname = speciesName)
    return headerText

def getDefensesTable(defense):
    tableHeader = '\n| ' + ' | '.join(defense.keys()) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---' for i in defense.keys()]) + ' :|\n'
    def getCol(v):
        if len(v) == 0:
            return '&nbsp;'
        else:
            return '<br>'.join(['![][{type}]'.format(type = i.lower()) for i in v])+'<br>'
    contentRow = '| ' + ' | '.join([getCol(v) for k,v in defense.items()]) + ' |\n'
    return tableHeader+separator+contentRow+'\n'

def getSpecies(mon):
    hyphenInd = mon.find('-')
    if('♂' in mon):
        form = 'base'
        species= 'nidoranu2642'
    elif '♀' in mon:
        form = 'base'
        species= 'nidoranu2640'
    elif 'Porygon-Z' == mon:
        form = 'base'
        species = 'porygonz'
    elif 'Ho-Oh' == mon:
        species = 'hooh'
        form = 'base'
    else:
        if hyphenInd == -1:
            form = 'base'
            species = mon.lower().strip()
        else:
            form = mon[hyphenInd+1:].strip().lower()
            species = mon[:hyphenInd].strip().lower()
        species = "".join([ c if c.isalnum() else "" for c in species ])
    return species, form

def getPokemonImage(name, form):
    num = speciesImageLookup[name.lower()]['NatDexNum']
    natDexNumber = f"{num:03}"
    imString = "![][{nm}_{f}]".format(nm=natDexNumber, f = form)
    fname = speciesImageLookup[name.lower()][form]
    pkmnInclude = "[{nm}_{f}]: ../img/animated/{fid}\n".format(nm=natDexNumber, f = form, fid=fname)
    return pkmnInclude, imString
    
def getEvolutionSection(evol):
    def evolString(entry):
        toMon = entry['To']
        method = entry['Method']
        if method == 'Happiness':
            method = 'Level up with max happiness'
        outString = '- [{toMon}]: {method}'.format(toMon=toMon, method = method)
        return outString
    def includeString(evol):
        toMon = evol['To']
        return '[{mon}]: ../{num}/'.format(mon=toMon, num=pokemonNumberMap[toMon])
    content = [evolString(entry) for entry in evol]
    incl = [includeString(entry) for entry in evol]
    return '\n'.join(incl)+'\n', \
                    '\n'.join(content)+'\n'

def getSpriteTypeTable(name, form, type):
    pkmnInclude, imString = getPokemonImage(name,form)
    tableHeader = '\n| ' + ' | '.join(['&nbsp;', 'Type']) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---' for i in ['&nbsp;', '&nbsp;']]) + ' :|\n'
    contentRow = '|' + '<br>'+imString + '|' + getSpeciesTypeString(type) + '|'
    return pkmnInclude, tableHeader+separator+contentRow+ '\n\n'

def getAbilityTable(abi):
    allHeaders = ['Ability 1', 'Ability 2', 'Hidden Ability']
    header = '| ' + ' | '.join(allHeaders[0:len(abi)]) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(abi)) + ' :|\n'
    content = '| ' + ' | '.join(abi) + ' |\n\n'
    return header + separator + content

def getStatTable(l_stats):
    stats = l_stats[0]
    if len(l_stats) > 1:
        vanilla_stats = l_stats[1]
        stat_diff = { k: stats[k]-vanilla_stats[k] for k in stats.keys()}
    else:
        stat_diff = { 0 for k in stats.keys()}
    cols = [i for i in stats.keys()]
    cols.append('BST')
    def get_header(t,d,w):
        if d == 0:
            return f"<th style=\"width:{w}%;align:center;vertical-align: middle;\">{t}</th>"
        if d > 0:
            s_diff_tag = 'sup'
            s_color = 'green'
            s_align = 'bottom'
            d = '+' + str(d)
        else:
            s_diff_tag = 'sub'
            s_color = 'red'
            s_align = 'top'
        return f"<th  style=\"width:{w}%;align:center;vertical-align: middle;color:{s_color};\">{t}<{s_diff_tag} style = \"line-height:0px;vertical-align: 5px;font-size: 10px;color:{s_color}\">{d}</{s_diff_tag}></th>"
    def getContentString(s,d,w):
        if d == 0:
            return f"<td style=\"width:{w}%;align:center;vertical-align: bottom;\">{s}</td>"
        if d > 0:
            s_diff_tag = 'sup'
            s_color = 'green'
            d = '+' + str(d)
        else:
            s_diff_tag = 'sub'
            s_color = 'red'
        return f"<td style=\"width:{w}%;align:center;vertical-align: middle;\">{s}<{s_diff_tag} style = \"color:{s_color}\">{d}</{s_diff_tag}></td>"
    
    content = [v for i,v in enumerate(stats.values())]
    content.append(sum(content))
    diff = [v for i,v in enumerate(stat_diff.values())]
    diff.append(sum(diff))
    width = [14, 14, 14, 14, 14, 14, 16]
    html_headers = [get_header(cols[t], diff[t], width[t]) for t in range(len(cols))]
    html_content = [getContentString(content[i],0,width[i]) for i in range(len(content))]
    header_row = "<tr>{h}</tr>".format(h=''.join(html_headers))
    content_row = "<tr>{h}</tr>".format(h=''.join(html_content))
    
    table_string = f'<table>{header_row}\n{content_row}</table>\n\n'

    return table_string

def getItemString(itemList):
    content = ['- {i}%: {j}'.format(i = item[0], j = item[1]) for item in itemList.items()]
    return '\n'.join(content)+'\n'

def getMoveData(movename):
    return [i for i in detailedMoveList if i['Name'].lower().replace(' ', '') == movename.lower().replace(' ', '')][0]


def getTMtable(moveList):
    def getTmDict(move):
        movedata = getMoveData(move['Name'])
        movedata['Machine'] = move['Machine']
        return movedata
    tmData = {i : getTmDict(move) for i, move in enumerate(moveList) }
    tableColumns = ['Machine', 'Name', 'Power', 'Accuracy', 'PP' ,'Type', 'Damage Class', 'Effect']
    tableHeader = '| ' + ' | '.join(tableColumns) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(tableColumns)) + ' :|\n'
    def makeTMRow(tm):
        row = '| ' + \
                str(tm['Machine']) + ' | ' + \
                tm['Name'] + ' | ' +\
                str(tm['Power']) + ' | ' +\
                str(tm['Accuracy']) + ' | ' +\
                str(tm['PP']) + ' | ' +\
                '![]['+tm['Type'].lower()+']' + ' | ' +\
                '![]['+tm['Damage Class'].lower()+']' + ' | ' +\
                'Priority: {prio}. {effect}'.format(prio = tm['Priority'], effect = str(tm['Effect']).replace('\n', '<br>')) + ' |'
        return row
    contentRows = [makeTMRow(data) for i,data in tmData.items()]
    return tableHeader+separator+'\n'.join(contentRows) +'\n\n'


def getLevelUpTable(moveList):
    def getLvlUpDict(move):
        movedata = getMoveData(move['Move'])
        movedata['Level'] = move['Level']
        return movedata
    lvlUpData =[ {i : getLvlUpDict(move)} for i, move in enumerate(moveList) ]
    tableColumns = ['Level', 'Name', 'Power', 'Accuracy', 'PP' ,'Type', 'Damage Class', 'Effect']
    tableHeader = '| ' + ' | '.join(tableColumns) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(tableColumns)) + ' :|\n'
    def makeLevelRow(i,level):
        level = level [i]
        row = '| ' + \
                str(level['Level']) + ' | ' + \
                level['Name'] + ' | ' +\
                str(level['Power']) + ' | ' +\
                str(level['Accuracy']) + ' | ' +\
                str(level['PP']) + ' | ' +\
                '![]['+level['Type'].lower()+']' + ' | ' +\
                '![]['+level['Damage Class'].lower()+']' + ' | ' +\
                'Priority: {prio}. {effect}'.format(prio = level['Priority'], effect = str(level['Effect']).replace('\n', '<br>')) + ' |'
        return row
    contentRows = [makeLevelRow(i,data) for i,data in enumerate(lvlUpData)]
    return tableHeader+separator+'\n'.join(contentRows) +'\n\n'


def getTutorTable(moveList):
    def getTutorDict(move):
        movedata = getMoveData(move)
        return movedata
    tutorData = {i : getTutorDict(move) for i, move in enumerate(moveList) }
    tableColumns = ['&nbsp;', 'Name', 'Power', 'Accuracy', 'PP' ,'Type', 'Damage Class','Effect']
    tableHeader = '| ' + ' | '.join(tableColumns) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(tableColumns)) + ' :|\n'
    def makeLevelRow(level):
        row = '| ' + \
                'Tutor' + ' | ' + \
                level['Name'] + ' | ' +\
                str(level['Power']) + ' | ' +\
                str(level['Accuracy']) + ' | ' +\
                str(level['PP']) + ' | ' +\
                '![]['+level['Type'].lower()+']' + ' | ' +\
                '![]['+level['Damage Class'].lower()+']' + ' | ' +\
                'Priority: {prio}. {effect}'.format(prio = level['Priority'], effect = str(level['Effect']).replace('\n', '<br>')) + ' |'
        return row
    contentRows = [makeLevelRow(data) for i,data in tutorData.items()]
    return tableHeader+separator+'\n'.join(contentRows) +'\n\n'

def getPreEvoMoveSection(moveList):
    tableColumns = ['Species', 'Method', 'Move']
    tableHeader = '| ' + ' | '.join(tableColumns) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(tableColumns)) + ' :|\n'
    def makeRow(entry):
        row = '| {species} | {method} | {move} |'.format(species = entry[0], method = entry[1], move = entry[2])
        return row
    contentRows = [makeRow(data) for data in moveList]
    return tableHeader+separator+'\n'.join(contentRows) +'\n\n'

def getEncounters(species):
    if(species != 'Ho-Oh' and '-' in species):
        formInd = species.find('-')
        species = species[:formInd].strip()
    def getSpeciesFromKey(k):
        formInd = k.find('-')
        if formInd !=-1:
            return k[:formInd].strip()
        return k
    wildEncounterKeys = [key for key in pokemonEncounters.keys() if species.lower() == getSpeciesFromKey(key).lower()]
    if len(wildEncounterKeys) == 0:
        return '',''
    def getForm(k):
        formInd = k.find('-')
        if formInd !=1:
            return k[formInd+1:].strip()
        return None
    encounterList = []
    if(len(wildEncounterKeys))>1:
        pokemonEncountersSubset = { getForm(k):pokemonEncounters[k] for k in wildEncounterKeys}
    else:
        pokemonEncountersSubset = pokemonEncounters[wildEncounterKeys[0]]
    def getPlaceLinkText(place):
        return '[{name}]'.format(name = place)
    def getPlaceLinkIncl(place):
        locationLinkKeys = list(locationLinks.keys())
        keysInPlace = [i for i in locationLinkKeys if i in place]
        locationSimilarity = [similar(place.lower(), i.lower()) for i  in keysInPlace]
        maxIndex = locationSimilarity.index(max(locationSimilarity))
        mostSimilarLocation = keysInPlace[maxIndex]
        # print(place, ',',mostSimilarLocation)
        return '[{name}]: ../../wildareas/{fname}'.format(name = place, fname = locationLinks[mostSimilarLocation].replace('.md', '/'))

    placeInclude = []
    
    unnested_encounters = unnest(pokemonEncountersSubset)
    unnested_encounters.sort(key = lambda item: tuple(i for i in item))
    if len(wildEncounterKeys) > 1:
        for row in unnested_encounters:
            form = row[0]
            location = row[1]
            data = row[-1]
            remaining_row = list(row)
            [remaining_row.pop(i) for i in [-1, 1, 0]]
            add_list = [[form, getPlaceLinkText(location), *remaining_row,e['Level'], round(e['Spawn Percent'],2)] for e in data]
            encounterList.extend(add_list)
            placeInclude.append(getPlaceLinkIncl(location))
    else:
        for row in unnested_encounters:
            data = row[-1]
            location = row[0]
            remaining_row = list(row)
            remaining_row.pop(0)
            remaining_row.pop(-1)
            add_list = [[getPlaceLinkText(location), *remaining_row,e['Level'], round(e['Spawn Percent'],2)] for e in data]
            encounterList.extend(add_list)
            placeInclude.append(getPlaceLinkIncl(location))
    placeInclude = '\n'.join(list(set(placeInclude)))
    n_cols = [len(e) for e in encounterList]
    max_cols = max(n_cols)
    colNames = ['&nbsp;']*max_cols
    colNames[-2] = 'Level'
    colNames[-1] = 'Spawn Percent'
    colNames[0] = 'Location'
    if len(wildEncounterKeys) > 1:
        colNames[0] = 'Form'
        colNames[1] = 'Location'
    
    adjusted_encounter_list = []
    for row in encounterList:
        this_length = len(row)
        missing_cols = max_cols - this_length
        row_list = list(row)
        [row_list.insert(-2,'&nbsp;') for i in range(missing_cols)]
        adjusted_encounter_list.append(row_list)
    topRow = '| ' + ' | '.join(colNames) + ' |\n'
    separator = '|: ' + ' :|: '.join(['--']*len(colNames)) + ' :|\n'
    content = ['| ' + ' | '.join([str(i) for i in row])  + ' |\n' for row in adjusted_encounter_list]
    tableString = topRow + separator + ''.join(content)
    return placeInclude,tableString


def isValid(item):
    if(item is None):
        return False
    if type(item) is not int and len(item) == 0:
        return False
    return True

def getSubsectionHeader(pkmnName):
    speciesName = pkmnName
    formMarkerInd = speciesName.find('-')
    if formMarkerInd == -1:
        headerName = speciesName
    else:
        headerName = speciesName[formMarkerInd:].replace('-','').strip()
    return '## {n}\n\n'.format(n=headerName)


def makePageText(pokemonInformation):
    pageSections = []
    bodyIncludes = []
    header_prepend = ""    
    if len(pokemonInformation) > 1:
        header_prepend = "#"
    elif len(pokemonInformation) == 0:
        raise TypeError
    for pkmn in pokemonInformation:
        if len(pokemonInformation) > 1:
             formHeader = getSubsectionHeader(pkmn['Name'])
             pageSections.append(formHeader)
        species, form = getSpecies(pkmn['Name'])
        pkmnInclude, tableString = getSpriteTypeTable(species,form = form, type = pkmn['TYPE'])
        bodyIncludes.append(pkmnInclude)
        pageSections.append(tableString)
        
        formKeys = [f for f in pkmn.keys() if isValid(pkmn[f])]

        if 'Defenses' in formKeys:
            pageSections.append(header_prepend+'## Defenses\n' + getDefensesTable(pkmn['Defenses']))
        if 'Ability' in formKeys:
            pageSections.append(header_prepend+'## Ability\n' + getAbilityTable(pkmn['Ability']))
        if 'STATS' in formKeys:
            stats = [pkmn['STATS']]
            if 'VANILLA STATS' in pkmn.keys():
                stats.append(pkmn['VANILLA STATS'])
            bstTable = getStatTable(stats)
            pageSections.append(header_prepend+'## Stats\n'+bstTable)
        if 'Items' in formKeys:
            pageSections.append(header_prepend+'## Wild Hold Items\n'+getItemString(pkmn['Items']))
        if 'Level Up  Moves' in formKeys:
            pageSections.append(header_prepend+'## Level Up Moves\n'+ getLevelUpTable(pkmn['Level Up Moves']))
        if 'TM Moves' in formKeys:
            pageSections.append(header_prepend+'## TM Moves\n' + getTMtable(pkmn['TM Moves']))
        if 'Tutor Moves' in formKeys:
            pageSections.append(header_prepend+'## Tutor Moves\n' + getTutorTable(pkmn['Tutor Moves']))
        if 'Evolutions' in formKeys:
            evolIncl, evolString = getEvolutionSection(pkmn['Evolutions'])
            pageSections.append(header_prepend+'## Evolutions\n'+evolString)        
            bodyIncludes.append(evolIncl) 
        if  'Pre-Evolution Moves' in formKeys:
            preEvoString = getPreEvoMoveSection(pkmn['Pre-Evolution Moves'])
            pageSections.append(header_prepend+'## Pre-Evolution Moves\n'+preEvoString)
    bodyText = '\n'.join(pageSections)
    return bodyIncludes, bodyText


def getPokemonMarkdown(pkmnInformation):
    headerText = getTopLevelHeader(pkmnInformation=pkmnInformation[0])
    page_includes, page_text = makePageText(pkmnInformation)
    tmp_incl = '\n'.join(page_includes)
    body_includes = "\n".join(list(OrderedDict.fromkeys(tmp_incl.split("\n"))))
    markdownText = '#' + headerText + '\n' + page_text
    includeText = '--8<-- "includes/abilities.md"\n\n' + getTypeIncludes() + body_includes + '\n'
    encounterIncl, encounterTable = getEncounters(pkmnInformation[0]['Name'])
    if encounterTable != '':
        markdownText += '\n## Encounter Locations\n\n'
        markdownText += encounterTable +'\n'
        includeText+=encounterIncl + '\n'
    markdownText += includeText
    number = pkmnInformation[0]['Number']
    natDexNumber = f"{number:03}"
    outfilename = natDexNumber+'.md'
    linkText = '- {htext}: pokemons/{fname}\n'.format(htext=headerText, fname = outfilename)
    return linkText, outfilename, markdownText