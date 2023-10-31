import re
import sys
import os
import json
from difflib import SequenceMatcher
from collections import OrderedDict
import tqdm

outLinkText = 'trainerscripts/out_trainerLinks.txt'
linkText = '  - Trainers By Area:\n'
fileDir = 'trainers/'
replacementString = '~~~~~~~~~~~~\nFirst Visit\n~~~~~~~~~~~~\n'
trainerListFile = 'trainerscripts/trainerList.txt'

# outLinkText = 'trainerscripts/out_postgameTrainerLinks.txt'
# linkText = '  - Postgame Trainers:\n'
# fileDir = 'postgame/'
# replacementString = '~~~~~~~~~~~~\nPostgame\n~~~~~~~~~~~~\n'
# trainerListFile = 'trainerscripts/postGameTrainers.txt'


# trainerListFile = 'trainerscripts/tmpTrainer.txt'
with open(trainerListFile, mode='r') as t:
    rawTrainerList = t.read()

legendTextFile = 'trainerscripts/legendText.txt'
with open(legendTextFile, mode = 'r') as l:
    legendText = l.read()

trainerImageList = os.listdir('./docs/img/Trainers')
trainerImageList = [i for i in trainerImageList if '.gif' in i]

pokemonImageLookup = './data/speciesImageLookup.json'
with open(pokemonImageLookup, 'r') as f:
    speciesImageLookup = json.load(f)



routeTitle = re.compile('={6,}\n(.+)\n={6,}\n')
secReg = re.compile('~{3,}\n(.+):*\n~{3,}')
notesReg = re.compile('- (.+)')
subSecReg = re.compile('~{1,} (.+) ~{1,}')



def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

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
        form = 'base'
        species = 'hooh'
    else:
        if hyphenInd == -1:
            form = 'base'
            species = mon.lower().strip()
        else:
            form = mon[hyphenInd+1:].strip().lower()
            species = mon[:hyphenInd].strip().lower()
        species = "".join([ c if c.isalnum() else "" for c in species ])
    return species, form

def getSplitReg(reg, raw):
    s = [m.start(0) for m in re.finditer(reg, raw)]
    s.insert(0,0)
    s.append(len(raw))
    s_list = [raw[s[i]:s[i+1]] for i in range(len(s)-1)]
    s_list = [i for i in s_list if i]
    return s_list

def makeNoteString(title,content):
    return '!!! {t}\n    {c}'.format(t = title, c = content)

def getNotesStrings(raw):
    notes = re.findall(notesReg, raw)
    outStr = ''
    for note in notes:
        if 'levels' in note.lower():
            title = 'Level-Info'
        else:
            title = 'Note'
        outStr+=makeNoteString(title, note)+'\n'
    return outStr

def getTabNameString(raw):
    match raw:
        case 'normal':
            return 'Easy and Normal Mode'
        case 'challenge':
            return 'Challenge Mode'
        case _:
            return raw.capitalize()

def offsetForTabs(raw):
    splitString = raw.split('\n')
    return '\n'.join(['    {text}'.format(text=s) for s in splitString])

def getPokemonCell(raw):
    monReg = re.compile('(.+) \[(.+)\], lv.(\d+)(?: @(.+))?: (.+)')
    monParts = re.findall(monReg, raw)[0]
    mon = monParts[0]
    abi = monParts[1]
    lv = monParts[2]
    item = monParts[3]
    moves = monParts[4]
    moveString = '<br>'.join(['• {n}'.format(n = m.strip()) for m in moves.split(',')])
    if item:
        pokeText = '{a}<br>Lv. {l}<br>{i}<br>{m}'.format(a = abi, l = lv, i = item, m = moveString)
    else:
        pokeText = '{a}<br>Lv. {l}<br>{i}<br>{m}'.format(a = abi, l = lv, i = '---', m = moveString)
    match mon:
        case 'F-00':
            pokePortraitString = '![][F00] <br> __{name}__ <br>'.format(name = mon)
            inclString = '[F00]: ../img/Misc/658.gif'
        case 'MT':
            pokePortraitString = '![][MT] <br> __{name}__ <br>'.format(name = mon)
            inclString = '[MT]: ../img/Misc/652.gif'
        case 'MT2':
            pokePortraitString = '![][MT2] <br> __{name}__ <br>'.format(name = mon)
            inclString = '[MT2]: ../img/Misc/653.gif'
        case 'UFO':
            pokePortraitString = '![][UFO] <br> __{name}__ <br>'.format(name = mon)
            inclString = '[UFO]: ../img/Misc/650.gif'
        case _:
            species, form = getSpecies(mon)
            thisMonImages = speciesImageLookup[species]
            thisMonIm = thisMonImages[form]
            imID = re.findall('(.+).gif', thisMonIm)[0]
            threeDigitNum = "{0:03}".format(thisMonImages['NatDexNum'])
            pokePortraitString = '![][{num}] <br> __[{name}]__ <br>'.format(num = imID, name = mon)
            inclString = '[{num}]: ../img/animated/{imStr}\n[{name}]: ../../pokemons/{natNum}/'\
                .format(num=imID, imStr =thisMonIm, name=mon, natNum=threeDigitNum)
    cell = pokePortraitString+pokeText
    return cell, inclString

def getTrainerImage(trainerName):
    match trainerName:
        case 'N':
            return 'Trainer_N.gif'
        case 'CHARLES':
            return 'Biker.gif'
        case 'Victini Guardian':
            return 'Veteran_Male.gif'
        case 'Hawes':
            return 'Scientist_Male.gif'
        case 'Gamefreak Morimoto':
            return 'Veteran_Male.gif'
        case 'Gamefreak Nishino':
            return 'Hiker.gif'
        case 'Clerk♂ Gilligan':
            return 'Clerk_Male_B.gif'
        case 'Black Kyruem':
            return '646-black.gif'     
        case 'White Kyurem':
            return '646-white.gif'     
        case _:      
            if('♂' in trainerName):
                trainerName = trainerName.replace('♂', ' Male')
            elif ('♀' in trainerName):
                trainerName = trainerName.replace('♀', ' Female')
            elif 'Plasma Grunt' in trainerName:
                return 'Plasma_Grunt_Male.gif'
            elif 'Hail Trainer' in trainerName or 'Rain Trainer' in trainerName:
                return 'Veteran_Female.gif'
            elif 'Sun Trainer' in trainerName or 'Sand Trainer' in trainerName:
                return 'Veteran_Male.gif'
            filenames = [i.replace('.gif','').replace('_', ' ') for i in trainerImageList]
            inName = [i for i in filenames if i.lower() in  trainerName.lower()]
            if len(inName) == 0:
                inName = filenames
            inNameSimilarity = [similar(trainerName.lower(), i.lower()) for i in inName]
            inNameMostSimilar = inName[inNameSimilarity.index(max(inNameSimilarity))]
            trainerImage = trainerImageList[filenames.index(inNameMostSimilar)]
            return trainerImage

def getTrainerCellStrings(trainerString):
    if '-' in trainerString:
        trainerLineReg = re.compile('(?:^([^A-z 0-9#,\n]+) )*([A-z 0-9#♂♀é,]+) - (.+)(?::)*')
        trainerInfo = re.findall(trainerLineReg, trainerString)[0]
        legendSymbols = trainerInfo[0]
        trainerName = trainerInfo[1]
        specialStrings = trainerInfo[2].replace(':', '')
    else:
        trainerLineReg = re.compile('(^[^A-z 0-9#,\n]+ )*([A-z 0-9#♂♀é,]+)(?::)*')
        trainerInfo = re.findall(trainerLineReg, trainerString)[0]
        legendSymbols = trainerInfo[0]
        trainerName = trainerInfo[1]
        specialStrings = ''
    if trainerName == 'Nate or Rosa':
        trainerPortraitString = '![][Nate]<br>![][Rosa]<br>__Nate or Rosa__'
        trainerIncl = '[Nate]: ../img/Trainers/Nate2.gif\n[Rosa]: ../img/Trainers/Rosa2.gif'
    else:
        trainerImage = getTrainerImage(trainerName)
        trainerNameString = trainerName.replace(' ', '').replace('#', '')
        trainerIncl = '[{trainerName}]: ../img/Trainers/{trainerImage}'\
                        .format(trainerName = trainerNameString, trainerImage = trainerImage)
        trainerPortraitString = '![][{imgString}]<br>__{trainerName}__'.format(imgString=trainerNameString, trainerName = trainerName)

    reward = re.findall('{(.+)}', specialStrings)
    battleType = re.findall('(\(.+\))', specialStrings)

    symbolString = legendSymbols if len(battleType)==0 else legendSymbols+battleType[0]
    rewardString = '' if len(reward)==0 else '<br>__Reward__<br>{r}'.format(r = reward[0])
    remainingText = re.sub('{(.+)}', '', specialStrings)
    remainingText = re.sub('(\(.+\))', '', remainingText).strip()

    secondCellContent = [remainingText, symbolString, rewardString]
    secondCellString = '<br>'.join([i for i in secondCellContent if i])

    trainerPortraitString='<br>'+trainerPortraitString+'<br>'+secondCellString
    return (trainerPortraitString, secondCellString), trainerIncl

def makeTrainerTable(trainerText):
    inclString = ''
    numPokemonCols = 3
    totalCols = 1 + numPokemonCols
    
    headers = ['Trainer', '&nbsp;', 'Pokémon', '&nbsp;']
    tmp = trainerText.splitlines()
    trainerLine = tmp[0]
    pokemon = tmp[1:]
    numRows = 2 if len(pokemon)>3 else 1
    cellContents = ['&nbsp;']*(totalCols*numRows)
    trainerCells, trainerIncl = getTrainerCellStrings(trainerLine)
    cellContents[0] = trainerCells[0]
    # cellContents[4] = trainerCells[1]
    pokemonIndices = [i for i in range(totalCols*numRows) if i not in [r*totalCols for r in range(numRows)]]
    inclString+=trainerIncl+'\n'
    for ind,mon in enumerate(pokemon):        
        tmppoke = getPokemonCell(mon)
        cellContents[pokemonIndices[ind]] = tmppoke[0]
        inclString+=tmppoke[1]+'\n'
    
    tableString = '| ' + ' | '.join(headers) + ' |\n'
    tableString +='|: ' + ' :|: '.join(['---']*len(headers)) + ' :|\n'
    rows = '\n'.join(['| '+' | '.join(cellContents[totalCols*(r):(r+1)*totalCols])+' |' for r in range(0,numRows)])+'\n'
    tableString+=rows
    
    inclString = "\n".join(list(OrderedDict.fromkeys(inclString.split("\n"))))

    return tableString, inclString

def makeComplexTrainerTable(rawString, depth =0):
    if '<' in rawString:
        splitString = rawString.splitlines()
        battleName = splitString[0]
        trainerLineReg = re.compile('(?:^([^A-z 0-9#,\n]+) )*([A-z 0-9#,]+) - (.+)(?::)*')
        trainerInfo = re.findall(trainerLineReg, battleName)[0]
        legendSymbols = trainerInfo[0]
        trainerName = trainerInfo[1]
        specialStrings = trainerInfo[2].replace(':', '')
        reward = re.findall('{(.+)}', specialStrings)
        battleType = re.findall('(\(.+\))', specialStrings)
        symbolString = legendSymbols if len(battleType)==0 else legendSymbols+battleType[0]
        rewardString = '' if len(reward)==0 else '    __Reward__: {r}\n'.format(r = reward[0])
        remainingText = re.sub('{(.+)}', '', specialStrings)
        remainingText = re.sub('(\(.+\))', '', remainingText).strip()
        trainerString = '=== "&nbsp; {t} &nbsp;"\n\n'.format(t = trainerName+' '+symbolString)
        if rewardString:
            trainerString+=rewardString
        interiorString, incl = getTrainerString('\n'.join(splitString[1:]), depth=depth+1)
        offsetString = offsetForTabs(interiorString)
        trainerString+=offsetString
        if depth ==0:
            trainerString+='\n&nbsp;'
    else:
        trainerString, incl = makeTrainerTable(rawString)
    return trainerString+'\n', incl

def getTrainerString(rawString, depth=0):
    if rawString == '':
        return rawString, ''
    elif '<' == rawString[0]:
        tabbedString = ''
        remainingString = rawString
        incl = ''
        tagReg = re.compile('<(.+)>')
        while(remainingString):
            tabName = re.search(tagReg, remainingString).group(1)
            tagInsideReg = re.compile('<{tag}>([\s\S]+)</{tag}>'.format(tag = tabName))
            tagContents = re.search(tagInsideReg, remainingString).group(1).strip()
            remainingString = re.sub(tagInsideReg, '', remainingString).strip()
            if tabName == 'text':
                tagContents = tagContents.replace('$$$', '\n').strip()
                tabbedString+=tagContents+'\n'
            else:
                localTab = '=== "{tn}"\n\n'.format(tn=getTabNameString(tabName))
                contentString = getTrainerString(tagContents, depth = depth +1)
                offsetString = offsetForTabs(contentString[0]) #need to add 4 spaces to the beginning of every line here...
                incl += contentString[1]
                localTab+=offsetString
                tabbedString += localTab + '\n'
                if not remainingString and depth == 0:
                    tabbedString+='&nbsp;\n'
        return tabbedString, incl
    elif '-' == rawString[0]:
        outStr = getNotesStrings(rawString)
        remainingString = re.sub(notesReg, '', rawString).strip()
        trainerString, incl = getTrainerString(remainingString, depth = depth+1)
        return outStr + trainerString, incl
    elif '$$$' in rawString:
        splitText = rawString.split('$$$')
        splitText = [i.strip() for i in splitText if i.strip()]
        cellContents = [getTrainerString(t.strip(), depth = depth+1) for t in splitText]
        trainerString = ''
        incl = ''
        for pair in cellContents:
            trainerString+=pair[0]+'\n'
            incl += pair[1]+'\n'
        return trainerString, incl
    else:
        trainerLine = rawString.splitlines()[0]
        if('(Tag)' in trainerLine or '(2x)' in trainerLine):
            trainerString, incl = makeComplexTrainerTable(rawString, depth = depth)
        else:
            trainerString, incl = makeTrainerTable(rawString)
        return trainerString, incl
    
def getSubSectionContent(rawSub):
    subsectionName = re.findall(subSecReg, rawSub)
    if len(subsectionName) == 0:
        subSecContent = ''
    else:
        subSecContent = '### {n}\n\n'.format(n = subsectionName[0])
    rawSubSecString = re.sub(subSecReg,'', rawSub).strip()
    if rawSubSecString == '':
        return '',''
    trainers = rawSubSecString.split('\n\n')
    trainers = [i.strip() for i in trainers if i.strip()]
    trainerStrings = [getTrainerString(s) for s in trainers]
    subSecContent += '\n'.join([t[0] for t in trainerStrings])+'\n'
    incl = '\n'.join([t[1] for t in trainerStrings])
    incl = "\n".join(list(OrderedDict.fromkeys(incl.split("\n"))))
    return subSecContent, incl

def getSectionContent(rawSection):
    sectionName = re.findall(secReg, rawSection)[0]
    rawSectionString = re.sub(secReg, '', rawSection).strip()
    if rawSectionString == '':
        return '',''
    subsections = getSplitReg(subSecReg, rawSectionString)
    subsectionStrings = [getSubSectionContent(s) for s in subsections]
    sectionContent = '\n'.join([t[0] for t in subsectionStrings]) +'\n'
    incl = '\n'.join([t[1] for t in subsectionStrings])
    incl = "\n".join(list(OrderedDict.fromkeys(incl.split("\n"))))
    sectionContent = '## {n}\n\n'.format(n=sectionName) + sectionContent 
    return sectionContent, incl

def getPageContent(rawPage):
    sections = getSplitReg(secReg, rawPage)
    sectionStrings = [getSectionContent(s) for s in sections]
    pageContent = '\n'.join([t[0] for t in sectionStrings])
    incl = '\n'.join([t[1] for t in sectionStrings])
    incl = "\n".join(list(OrderedDict.fromkeys(incl.split("\n"))))
    return pageContent, incl


routeList = getSplitReg(routeTitle, rawTrainerList)
for route in tqdm.tqdm(routeList):
    #get and remove the route title
    pageTitle = re.findall(routeTitle, route)[0]
    secRoute = re.sub(routeTitle, replacementString, route)
    pageStr, incl = getPageContent(secRoute)

    pageStr = pageStr.replace('●', ':exclamation:')
    pageStr = pageStr.replace('○', ':grey_exclamation:')
    pageStr = pageStr.replace('♕', ':warning:')
    pageStr = pageStr.replace('♛', ':warning:')
    pageStr = pageStr.replace('(2x)', ':two:')
    pageStr = pageStr.replace('(3x)', ':three:')
    pageStr = pageStr.replace('(Tag)', ':handshake:')
    pageStr = pageStr.replace('(Rot)', ':arrows_counterclockwise:')

    if pageTitle == 'Village Bridge':
        pageStr = pageStr.replace('*', ':sparkles:')

    pageContent = '# {n}\n\n'.format(n = pageTitle) + legendText + '\n\n' + pageStr

    

    incl = '--8<-- "includes/abilities.md"\n' + '--8<-- "includes/held_items.md"\n' + incl
    filename = fileDir+"".join([ c if c.isalnum() else "" for c in pageTitle.lower()])+'.md'
    with open('docs/'+filename, 'w') as f:
        f.write(pageContent+'\n\n\n'+incl)
    linkText+='    - {linkName}: {path}\n'.format(linkName = pageTitle, path=filename)

with open(outLinkText,'w') as f:
    f.write(linkText)