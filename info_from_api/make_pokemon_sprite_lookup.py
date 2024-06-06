import os
import csv
import re
import tqdm
import json

spriteFolder = './docs/img/animated/'
spriteList = os.listdir(spriteFolder)
spriteList = [i for i in spriteList if '.gif' in i]

pokemonIndexFile = './data/pokemonNumberName.csv'
with open(pokemonIndexFile, 'r', encoding='utf-8-sig') as indexFile:
    reader = csv.reader(indexFile)
    pokemonNumberMap = { int(row[1]):row[2] for row in reader}

numeric = re.compile('([0-9]+)')
remainingSprites = spriteList
imageLookup = {}

formNameReg = re.compile('(?:[0-9]+)-([A-z]+).gif')
def getFormName(i):
    fn = re.findall(formNameReg, i)
    if len(fn) == 0:
        return 'base'
    thisForm = fn[0]
    if 'question' == thisForm:
        formName = '?'
    elif 'exclamation' == thisForm:
        formName = '!'
    else:
        formName = thisForm
    return formName

for num in tqdm.tqdm(range(1,650)):
    relatedIm = [i for i in remainingSprites if int(re.findall(numeric, i)[0]) == num]
    formImMap = {getFormName(i):i for i in relatedIm}
    formImMap['NatDexNum'] = num
    species = pokemonNumberMap[num].lower()
    species = "".join([ c if c.isalnum() else "" for c in species ])
    imageLookup[species] = formImMap
    remainingSprites = [i for i in remainingSprites if i not in relatedIm]

outFile = './data/speciesImageLookup.json'
tmp = json.dumps(imageLookup)
with open(outFile, mode = 'w') as f:
    f.write(tmp)