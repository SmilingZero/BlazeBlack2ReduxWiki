from genericpath import isfile
import os
import tqdm
import json
import csv
import re

dataDir = 'data/'
moveListFile = 'moveList.csv'
listMoveChanges = 'moveChangeList.txt'

databaseMoveData = 'temp/move/'
dbMoveFiles = os.listdir(databaseMoveData)

def getint(name):
    basename = name.partition('.')
    return int(basename[0])
dbMoveFiles.sort(key=getint)

# Get initial listing for moves...
with open(dataDir+moveListFile, mode = 'r') as listFile:
    reader = csv.reader(listFile)
    moves = [rows[1] for rows in reader]

moveListKeys = ['Name', 'Power', 'PP', 'Accuracy', 'Type', 'Damage Class', 'Effect', 'Priority']
detailedMoveList = [dict.fromkeys(moveListKeys) for i in range(len(moves))]
for ind,move in enumerate(tqdm.tqdm(moves)):
    movename = move.lower()
    movename = re.sub('[^0-9a-zA-Z]+', '', movename)
    foundFile = False
    for tind,testfile in enumerate(dbMoveFiles):
        with open(databaseMoveData+testfile) as testmove:
            tmove = json.load(testmove)
        tmovename = re.sub('[^0-9a-zA-Z]+', '', tmove['name'])
        if tmovename.lower() == movename:
            detailedMoveList[ind]['Name'] = move.strip()
            detailedMoveList[ind]['Power'] = tmove['power']
            detailedMoveList[ind]['PP'] = tmove['pp']
            detailedMoveList[ind]['Accuracy'] = tmove['accuracy']
            detailedMoveList[ind]['Type'] = tmove['type']['name']
            detailedMoveList[ind]['Damage Class'] = tmove['damage_class']['name']
            detailedMoveList[ind]['Priority'] = tmove['priority']
            if(len(tmove['effect_entries'])>0):
                effectText = tmove['effect_entries'][0]['effect'].replace('Inflicts regular damage. ', '').strip()
                if '$effect_chance' in effectText:
                    effectText = effectText.replace('$effect_chance', str(tmove['effect_chance']))
                detailedMoveList[ind]['Effect'] = effectText
            dbMoveFiles.remove(testfile)
            foundFile = True
            break
    if not foundFile:
        print('stop')
            
# Load list of move changes
with open(dataDir + listMoveChanges) as moveChangeFile:
    changeText = moveChangeFile.read()

moveChanges = changeText.split('\n\n')
for ind,entry in enumerate(tqdm.tqdm(moveChanges)):
    lines = entry.splitlines()
    moveName = lines[0].strip()
    matchingMoveInd = [i for i, move in enumerate(detailedMoveList) if move['Name'] == moveName]
    changes = lines[1:]
    for cind, change in enumerate(changes):
        key = re.search('([a-zA-z]+)', change)[0].strip()
        content = change[re.search('(->)', change).start()+2 :].strip()
        endInd = content.find('[')
        if endInd != -1:
            content = content[: endInd].strip()
        content = re.search('([^\*]+)', content)[0]
        if key in ['Power', 'PP', 'Priority']:
            content = int(content)
        detailedMoveList[matchingMoveInd[0]][key] = content


os.makedirs('scrapedJSON/ref/', exist_ok = True)
json_string = json.dumps(detailedMoveList, indent=4, ensure_ascii=True)
with open('scrapedJSON/ref/moves_with_descriptions.json', 'w', encoding = 'utf-8') as f:
    f.write(json_string)

print('stop')