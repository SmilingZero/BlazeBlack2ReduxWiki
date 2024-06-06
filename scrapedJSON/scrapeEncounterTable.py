import re;
import json;

def sanitizeEncounterTable(s):
    s_string = json.dumps(s)
    s_string = s_string.replace('Shellos-E','Shellos-East')
    s_string = s_string.replace('Shellos-W','Shellos-West')
    s_string = s_string.replace('Gastrodon-W','Gastrodon-West')
    s_string = s_string.replace('Gastrodon-E','Gastrodon-East')
    s_string = s_string.replace('Basculin-R','Basculin-Red')
    s_string = s_string.replace('Basculin-B','Basculin-Blue')
    s_string = s_string.replace('Darmanitan-Z','Darmanitan-Zen')
    s_string = s_string.replace('Cherrim -S','Cherrim - Sunshine')
    s_string = s_string.replace('Whiripede','Whirlipede')

    s_string = s_string.replace('Grass, Normal','Grass')
    s_string = s_string.replace('Grass, Doubles','Dark Grass (Doubles)')
    s_string = s_string.replace('Grass, Shaking Spots','Shaking Grass')
    s_string = s_string.replace('Surf, Normal','Surf')
    s_string = s_string.replace('Surf, Dark Spot','Surf, Rippling Water')
    s_string = s_string.replace('Fish, Normal','Fish')
    s_string = s_string.replace('Fish, Dark Spot','Fish, Rippling Water')
    s_string = s_string.replace('Sand, Normal','Sand')
    s_string = s_string.replace('Cave, Normal','Cave')
    s_string = s_string.replace('Cave, Dust Clouds','Dust Clouds')
    s_string = s_string.replace('Sewer, Normal','Sewer')
    s_string = s_string.replace('Swamps, Normal','Swamps')
    s_string = s_string.replace('Bridge, Dark Spots','Shadows')
    s_string = s_string.replace('Cave, Dust Cloud','Dust Clouds')
    s_string = s_string.replace('Dust Clouds', 'Dust Cloud')
    
    s_string = s_string.replace('Underground Ruins - All Areas','Underground Ruins')

    return json.loads(s_string)

# Pull in all text from the doc
filename = './scrapedJSON/ref/Wild Area Changes.txt'
with open(filename, 'r') as file:
    data = file.read()

# Define REGEX Patterns
mainHeaderPattern = '(={9,})\n([a-zA-z ]+)\n(={9,})\n'
mainHeaderReg = re.compile(mainHeaderPattern)
areaHeaderPattern = '(~{4,})([ a-zA-z0-9\-,\'():\/]+)(~{4,})'
areaHeaderReg = re.compile(areaHeaderPattern)

# Slice doc according to sections
def sliceTextByReg(reg, text):
    mainHeaderStarts = [m.start(0) for m in re.finditer(reg, text)]
    mainHeaderStarts.insert(0, 0)

    splitText = []
    sectionName = []
    for startInd, start in enumerate(mainHeaderStarts):
        if(startInd == len(mainHeaderStarts)-1):
            thisText =  text[start:]
        else:
            thisText = (text[start:mainHeaderStarts[startInd+1]])
        thisHeader = re.findall(reg, thisText)
        if len(thisHeader)==0:
            sectionName.append('Top')
            totalLength = 0;
        else:
            totalLength = sum([len(x) for x in thisHeader[0]])
            sectionName.append(thisHeader[0][1])
        splitText.append(thisText[totalLength:]);
    return sectionName, splitText

mainSectionNames, splitDoc = sliceTextByReg(mainHeaderReg, data)

# Grab "tabular" sections - stored by the "main/post" sections...
tabularSections = ['Main Story', 'Postgame Locations']
parsedSections = {}
grottoDict = {}
grottoFlags = ['Common Encounters:', 'Uncommon Encounters:', 'Rare Encounters:']
grottoPokemonPercent = 1;
grottoEncounterPercents = {'Common': 15, 'Uncommon': 4, 'Rare':1}
for ind,sec in enumerate(splitDoc):
    if mainSectionNames[ind] in tabularSections:
        thisSection = sec
        secNames, splitSection = sliceTextByReg(areaHeaderReg, thisSection)
        parsedSection = {secNames[i].strip(): splitSection[i] for i in range(len(secNames))}
        parsedSection.pop("Top", None)
        parsedSections[mainSectionNames[ind]] = parsedSection
    if "Hidden Grotto Guide" in mainSectionNames[ind]:
        grottoText = sec
        secNames, splitSection = sliceTextByReg(areaHeaderReg, grottoText)
        parsedGrotto = {secNames[i].strip(): splitSection[i] for i in range(len(secNames))}
        parsedGrotto.pop("Top", None)
        for routeName, encounters in parsedGrotto.items():
            theseEncounters = [x for x in encounters.splitlines() if x.strip()]
            subgroupHeaderMask = [(x in grottoFlags) for x in theseEncounters]
            subgroupHeaderInd = [i for i, x in enumerate(subgroupHeaderMask) if x]
            tmpGrottoGroup = {}
            for gInd, subgroup in enumerate(subgroupHeaderInd):
                if(gInd == len(subgroupHeaderInd)-1):
                    group = theseEncounters[subgroup:]
                else:
                    group = theseEncounters[subgroup:subgroupHeaderInd[gInd+1]]
                mons = [x[2:].strip() for x in group[1:]]
                rate = re.search('([a-zA-z0-9\-,]+)', group[0])[0]
                totalRate = float(grottoEncounterPercents[rate])/grottoPokemonPercent
                eachMonPercent = totalRate / len(mons)
                for i in range(len(mons)):
                    tmpGrottoGroup[mons[i]] =  [{'Level': '??', 'Spawn Percent': eachMonPercent}]
            grottoDict[routeName] = tmpGrottoGroup

pokemonRegex = re.compile('([0-9A-Za-z *.♂♀\-?!\']+)(Lv. [0-9\-]+ )([0-9\-]+%)')
encounterTypeRegex = re.compile('([a-zA-Z0-9, ]+):')
specialConditionFlag = 'Hidden Grotto'

completeEncounters = {};
for sectionOfGame, locations in parsedSections.items():
    thisSectionEncounters = {}
    for routeName, encounters in locations.items():
        encountersSplitLine = [x for x in encounters.splitlines() if x]
        # Take all of the lines and hold the "second column" in quarantine... 
        encounterTextList = []
        col2List = []
        for line in encountersSplitLine:
            if(len(line) > 40):
                encounterTextList.append(line[:40].strip())
                col2List.append(line[40:].strip())
            else:
                encounterTextList.append(line)
        [encounterTextList.append(x) for x in col2List]
        tmpEncounterTable = {}
        encounterTable = {}
        currentEncounterType = None
        tmpMon = {}
        for lineInd, line in enumerate(encounterTextList):
            storeData = False
            resetEncounterType = False
            isLast = lineInd+1 == len(encounterTextList)
            pkmnEntry = re.findall(pokemonRegex, line)
            encounterTypeEntry = re.findall(encounterTypeRegex, line)
            
            if(len(pkmnEntry)>0):
                # unpack the line and break it into a dict for hte pokemon; add it to the current group?
                tmpMon['Level'] = re.findall('([0-9\-]+)', pkmnEntry[0][1])[0]
                stringPerc = re.findall('([0-9\-]+)', pkmnEntry[0][2])[0]
                if(stringPerc == '--'):
                    stringPerc = '100'
                tmpMon['Spawn Percent'] = float(stringPerc)
                encounterTableKey = re.findall('([A-Za-z0-9 .♂♀\-?!\']+)', pkmnEntry[0][0])[0].strip()
                if encounterTableKey not in tmpEncounterTable:
                    tmpEncounterTable[encounterTableKey] = [tmpMon]
                else:
                    currentEntry = tmpEncounterTable[encounterTableKey]
                    levelRanges = [e['Level'] for e in currentEntry]
                    if tmpMon['Level'] in levelRanges:
                        tmpEncounterTable[encounterTableKey][levelRanges.index(tmpMon['Level'])]['Spawn Percent'] += tmpMon['Spawn Percent']
                    else:
                        tmpEncounterTable[encounterTableKey].append(tmpMon)
                tmpMon = {}

            if len(encounterTypeEntry) > 0:
                if currentEncounterType is not None:
                    storeData = True
                resetEncounterType = True
                    
            if(isLast and currentEncounterType is not None):
                storeData = True
            if(storeData):
                encounterTable[currentEncounterType] = tmpEncounterTable
                tmpEncounterTable = {}
            if(resetEncounterType):
                currentEncounterType = encounterTypeEntry[0]
            if(currentEncounterType is not None and 'Grotto' in currentEncounterType):
                
                for key in grottoDict:
                    if ':' in key:
                        stripkey = re.search('([A-Za-z0-9 \-]+):', key)[0].strip()
                        stripkey = stripkey.replace(':','')
                    else:
                        stripkey = re.search('([A-Za-z0-9 \-]+)', key)[0].strip()
                    if stripkey in routeName:
                        if 'Pinwheel Forest' in routeName:
                            eveve = 1
                        locInd = key.rfind(':')
                        keyName = ''
                        if(locInd != -1):
                            keyName = key[locInd:]
                        keyName = 'Hidden Grotto' + keyName;
                        encounterTable[keyName] = grottoDict[key]
                currentEncounterType = None
        encounterTable = sanitizeEncounterTable(encounterTable)
        thisSectionEncounters[routeName.strip()] = encounterTable
    packedEncounters = {}
    if 'Main' in sectionOfGame:
        packedEncounters['Virbank Complex - Inside'] = thisSectionEncounters['Virbank Complex - Inside']
        packedEncounters['Virbank Complex - Outside'] = thisSectionEncounters['Virbank Complex - Outside']
        thisSectionEncounters.pop('Virbank Complex - Inside')
        thisSectionEncounters.pop('Virbank Complex - Outside')
    if 'Postgame' in sectionOfGame:
        packedEncounters['Pinwheel Forest - Inside'] = thisSectionEncounters['Pinwheel Forest - Inside']
        packedEncounters['Pinwheel Forest - Outside'] = thisSectionEncounters['Pinwheel Forest - Outside']
        thisSectionEncounters.pop('Pinwheel Forest - Inside')
        thisSectionEncounters.pop('Pinwheel Forest - Outside')
    keysInThisSection = thisSectionEncounters.keys()
    baseKey = list(set([re.search('[a-zA-Z0-9 ]+', x)[0].strip() for x in keysInThisSection]))
    baseKey = [x for x in baseKey if x != 'Virbank Complex' or x != 'Pinwheel Forest']
    for thisKey in baseKey:
        matchingKeys = [x for x in keysInThisSection if thisKey == re.search('([A-Za-z0-9 ]+)', x)[0].strip()]
        if(len(matchingKeys) == 1):
            packedEncounters[matchingKeys[0]] = thisSectionEncounters[matchingKeys[0]]
            continue
        tmpInnerDict = {}
        for mKey in matchingKeys:
            innerKey = re.search('([A-Za-z0-9, ]+)', mKey.replace(thisKey, '').strip())[0].strip()
            tmpInnerDict[innerKey] = thisSectionEncounters[mKey]
        packedEncounters[thisKey] = tmpInnerDict
    completeEncounters[sectionOfGame.strip()] = packedEncounters
    

allEncountersJSON = json.dumps(completeEncounters, indent = 4)
with open("./scrapedJSON/ref/nestedEncounterTable.json", "w") as outfile:
    outfile.write(allEncountersJSON)