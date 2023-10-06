from genericpath import isfile
import os
import tqdm
import json
import csv
import re

def getint(name):
    basename = name.partition('.')
    return int(basename[0])

os.makedirs('docs/pokemons')
pkmnDir = 'scrapedJSON/pokemon/'
listOfPokemonFiles = os.listdir(pkmnDir)
listOfPokemonFiles.sort(key=getint)
moveList = 'scrapedJSON/ref/moves_with_descriptions.json'

for ind, jsonFile in enumerate(listOfPokemonFiles):
    with open(pkmnDir+jsonFile) as pkmnFile:
        fileInformation = json.load(pkmnFile)
        markdownString = ''
    print('stop')