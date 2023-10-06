from genericpath import isfile
import os
import tqdm
import json
import csv
import re
import pokemonDocWriter as pkmnWriter

def getint(name):
    basename = name.partition('.')
    return int(basename[0])

docOutFolder = 'docs/pokemons/'
os.makedirs(docOutFolder, exist_ok=True)
pkmnDir = 'scrapedJSON/pokemon/'
listOfPokemonFiles = os.listdir(pkmnDir)
listOfPokemonFiles.sort(key=getint)
moveList = 'scrapedJSON/ref/moves_with_descriptions.json'



for ind, jsonFile in enumerate(listOfPokemonFiles):
    with open(pkmnDir+jsonFile) as pkmnFile:
        pkmnInformation = json.load(pkmnFile)
    outfilename, markdownText = pkmnWriter.getPokemonMarkdown(pkmnInformation)
    with open(docOutFolder+outfilename, mode='w') as outputMarkdown:
        outputMarkdown.write(markdownText)
    print('stop')