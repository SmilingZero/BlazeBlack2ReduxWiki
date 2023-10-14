import os
import json
import csv
from collections import OrderedDict

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

def getPokemonImage(number, form):
    natDexNumber = f"{number:03}"
    imString = "![][{nm}_{f}]".format(nm=natDexNumber, f = form)
    fname = str(number)+'_'+str(form)+'.png'
    pkmnInclude = "[{nm}_{f}]: ../img/pokemon/{fid}\n".format(nm=natDexNumber, f = form, fid=fname)
    return pkmnInclude, imString
    
def getEvolutionSection(evol):
    def evolString(entry):
        toMon = entry['To']
        method = entry['Method']
        outString = '- [{toMon}]: {method}'.format(toMon=toMon, method = method)
        return outString
    def includeString(evol):
        toMon = evol['To']
        return '[{mon}]: ./{num}/'.format(mon=toMon, num=pokemonNumberMap[toMon])
    content = [evolString(entry) for entry in evol]
    incl = [includeString(entry) for entry in evol]
    return '\n'.join(incl)+'\n', \
                    '\n'.join(content)+'\n'


def getSpriteTypeTable(number, form, type):
    pkmnInclude, imString = getPokemonImage(number,form)
    tableHeader = '\n| ' + ' | '.join(['&nbsp;', 'Type']) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---' for i in ['&nbsp;', '&nbsp;']]) + ' :|\n'
    contentRow = '|' + imString + '|' + getSpeciesTypeString(type) + '|'
    return pkmnInclude, tableHeader+separator+contentRow+ '\n\n'

def getAbilityTable(abi):
    allHeaders = ['Ability 1', 'Ability 2', 'Hidden Ability']
    header = '| ' + ' | '.join(allHeaders[0:len(abi)]) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(abi)) + ' :|\n'
    content = '| ' + ' | '.join(abi) + ' |\n\n'
    return header + separator + content

def getStatTable(stats):
    cols = [i for i in stats.keys()]
    cols.append('BST')
    content = [v for i,v in enumerate(stats.values())]
    content.append(sum(content))
    vals = [str(i) for i in content]
    header = '| ' + ' | '.join(cols) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(cols)) + ' :|\n'
    content = '| ' + ' | '.join(vals) + ' |\n\n'
    return header + separator + content

def getItemString(itemList):
    content = ['- {i}'.format(i = item) for item in itemList]
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
    return '', tableHeader+separator+'\n'.join(contentRows) +'\n\n'


def getLevelUpTable(moveList):
    def getLvlUpDict(move):
        movedata = getMoveData(move['Move'])
        movedata['Level'] = move['Level']
        return movedata
    lvlUpData = {i : getLvlUpDict(move) for i, move in enumerate(moveList) }
    tableColumns = ['Level', 'Name', 'Power', 'Accuracy', 'PP' ,'Type', 'Damage Class', 'Effect']
    tableHeader = '| ' + ' | '.join(tableColumns) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(tableColumns)) + ' :|\n'
    def makeLevelRow(level):
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
    contentRows = [makeLevelRow(data) for i,data in lvlUpData.items()]
    return '', tableHeader+separator+'\n'.join(contentRows) +'\n\n'


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
    return '', tableHeader+separator+'\n'.join(contentRows) +'\n\n'

def getPokemonMarkdown(pkmnInformation):
    headerText = getTopLevelHeader(pkmnInformation=pkmnInformation[0])
    if len(pkmnInformation)==1:
        bodyIncludes, bodyText = getSingleFormMarkdown(pkmnInformation[0])
    else:
        bodyText = ''
        formIncludes = []
        for ind,form in enumerate(pkmnInformation):
            incl, formText = getMultiFormMarkdown(form, ind)
            bodyText+= formText+'\n'
            [formIncludes.append(i) for i in incl]
        tmpIncludes = '\n'.join(formIncludes)
        bodyIncludes = "\n".join(list(OrderedDict.fromkeys(tmpIncludes.split("\n"))))
    markdownText = '#' + headerText + '\n' + bodyText
    includeText = '--8<-- "includes/abilities.md"\n\n' + getTypeIncludes() + bodyIncludes + '\n'
    
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
    colNames = ['Form', 'Location', 'Encounter Type', 'Level', 'Encounter Percent']
    if len(wildEncounterKeys) > 1:
        pokemonEncountersSubset = { getForm(k):pokemonEncounters[k] for k in wildEncounterKeys}
        [[[encounterList.append([form, place, method, encounter['Level'], round(encounter['Spawn Percent'], 2)]) for method, encounter in methods.items()]for place, methods in places.items() ]for form,places in pokemonEncountersSubset.items()]
        topRow = '| ' + ' | '.join(colNames) + ' |\n'
        separator = '|: ' + ' :|: '.join(['--']*len(colNames)) + ' :|\n'
        content = ['| ' + ' | '.join([str(i) for i in row])  + ' |\n' for row in encounterList]
        tableString = topRow + separator + ''.join(content)
        return '',tableString
    else:
        pokemonEncountersSubset = pokemonEncounters[wildEncounterKeys[0]]
        [[encounterList.append([place, k, v['Level'], round(v['Spawn Percent'],2)]) for k,v in method.items()] for place, method in pokemonEncountersSubset.items()]
        topRow = '| ' + ' | '.join(colNames[1:]) + ' |\n'
        separator = '|: ' + ' :|: '.join(['--']*len(colNames[1:])) + ' :|\n'
        content = ['| ' + ' | '.join([str(i) for i in row])  + ' |\n' for row in encounterList]
        tableString = topRow + separator + ''.join(content)
        return '',tableString

def getSingleFormMarkdown(pkmnInformation):
    bodyText = ''
    bodyIncludes = ''
    number = pkmnInformation['Number']
    pkmnInclude, tableString = getSpriteTypeTable(number,form = 0, type = pkmnInformation['TYPE'])
        
    abilityTable = getAbilityTable(pkmnInformation['Ability'])
    bstTable = getStatTable(pkmnInformation['STATS'])
    bodyText+=tableString
    bodyText+='## Defenses\n\n'
    bodyText+= getDefensesTable(pkmnInformation['Defenses'])
    bodyText+= '## Ability\n\n'
    bodyText+=abilityTable
    bodyText+='## Stats\n\n'
    bodyText+=bstTable
    bodyIncludes+=pkmnInclude
    if len(pkmnInformation['Items']) > 0:
        bodyText+= '## Wild Hold Items\n'
        bodyText += getItemString(pkmnInformation['Items'])
    if len(pkmnInformation['Level Up Moves']) >0:
        bodyText += '## Level Up Moves\n'
        lvlUpIncludes, levelUpTable = getLevelUpTable(pkmnInformation['Level Up Moves'])
        bodyText+= levelUpTable
    if len(pkmnInformation['TM Moves']) >0:
        bodyText += '## TM Moves\n'
        tmIncludes, tmTable = getTMtable(pkmnInformation['TM Moves'])
        bodyText+= tmTable
    if len(pkmnInformation['Tutor Moves']) >0:
        bodyText += '## Tutor Moves\n'
        tutorIncludes, tutorTable = getTutorTable(pkmnInformation['Tutor Moves'])
        bodyText+= tutorTable
    if len(pkmnInformation['Evolutions'])>0:
        bodyText += '## Evolution\n'
        evolInclude, evolString = getEvolutionSection(pkmnInformation['Evolutions'])
        bodyText += evolString
        bodyIncludes += evolInclude
    return bodyIncludes, bodyText

def getSubsectionHeader(pkmnName):
    speciesName = pkmnName
    formMarkerInd = speciesName.find('-')
    if formMarkerInd == -1:
        headerName = speciesName
    else:
        headerName = speciesName[formMarkerInd:].replace('-','').strip()
    return '## {n}\n\n'.format(n=headerName)


def getMultiFormMarkdown(pkmn,form):
    bodyText = ''
    bodyIncludes = []
    number = pkmn['Number']
    formHeader = getSubsectionHeader(pkmn['Name'])
    bodyText+=formHeader
    pkmnInclude, tableString = getSpriteTypeTable(number,form = form, type = pkmn['TYPE'])
    bodyText+= tableString
    bodyIncludes.append(pkmnInclude)
    def isValid(item):
        if(item is None):
            return False
        if type(item) is not int and len(item) == 0:
            return False
        return True
    formKeys = [f for f in pkmn.keys() if isValid(pkmn[f])]
    if 'Defenses' in formKeys:
        bodyText+='### Defenses\n'
        bodyText+= getDefensesTable(pkmn['Defenses'])
    if 'Ability' in formKeys:
        bodyText+='### Ability\n'
        bodyText+=getAbilityTable(pkmn['Ability'])
    if 'STATS' in formKeys:
        bodyText+='### Stats\n'
        bodyText+= getStatTable(pkmn['STATS'])
    if 'Items' in formKeys:
        bodyText+='### Wild Hold Items\n'
        bodyText+= getItemString(pkmn['Items'])
    if 'Level Up Moves' in formKeys:
        bodyText += '### Level Up Moves\n'
        incl, string = getLevelUpTable(pkmn['Level Up Moves'])
        bodyText += string
    if 'TM Moves' in formKeys:
        bodyText += '### TM Moves\n'
        incl, string = getTMtable(pkmn['TM Moves'])
        bodyText += string
    if 'Tutor Moves' in formKeys:
        bodyText += '### Tutor Moves\n'
        incl, string = getTutorTable(pkmn['Tutor Moves'])
        bodyText += string
    if 'Evolutions' in formKeys:
        bodyText += '### Evolutions\n'
        evolIncl, evolString = getEvolutionSection(pkmn['Evolutions'])
        bodyText += evolString
        bodyIncludes.append(evolIncl)
    return bodyIncludes, bodyText