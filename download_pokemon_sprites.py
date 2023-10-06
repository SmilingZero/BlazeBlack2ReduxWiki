
from genericpath import isfile
import os
import requests
import tqdm
import json

imageDir = "img/pokemon/"
os.makedirs(imageDir,exist_ok=True)
scrapedJSONDir = 'scrapedJSON/pokemon/'
scrapedPkmnFiles = os.listdir(scrapedJSONDir)

tempDir = 'temp/pokemon/'
tempPokemonFiles = os.listdir(tempDir)

for fid in tqdm.tqdm(scrapedPkmnFiles):
    with open(scrapedJSONDir + fid) as pkmnJson:
        data = json.load(pkmnJson)
        for monInd,mon in enumerate(data):
            imName = str(mon['Number'])+'_'+str(monInd)+'.png'
            if os.path.isfile(imageDir+imName):
                try:
                    tempPokemonFiles.remove(str(mon['Number']).lstrip()+'.json')
                except ValueError:
                    pass
                continue
            name = mon['Name'].lower().replace(' ', '').replace('-', '').replace('.', '').replace('’', '')
            fileFound = None
            for tmpFile in tempPokemonFiles:
                with open(tempDir + tmpFile) as pkmnTmp:
                    tmpData = json.load(pkmnTmp)
                    tmpName = tmpData['name'].lower().replace(' ', '').replace('-', '').replace('.', '').replace('’', '')
                    saveFlag = name == tmpName
                    if name == 'basculin':
                        saveFlag = name in tmpName
                    if saveFlag:
                        spriteurl = tmpData['sprites']['front_default']
                        response = requests.get(spriteurl)
                        fileFound = tmpFile
                        with open(imageDir+imName, 'wb') as f:
                            f.write(response.content)
                        tempPokemonFiles.remove(tmpFile)
                        break
            if fileFound is None:
                dsovbnweounwoevue = 1
                    
   
