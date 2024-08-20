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
listOfPokemonFiles = [f for f in os.listdir(pkmnDir) if f.endswith('.json')]
# listOfPokemonFiles = ['413.json']
listOfPokemonFiles.sort(key=getint)
moveList = 'scrapedJSON/ref/moves_with_descriptions.json'

pokemonLinkTextFile = 'pokemonNavLinks.txt'

allLinkText = ''
for ind, jsonFile in enumerate(tqdm.tqdm(listOfPokemonFiles)):
    with open(pkmnDir+jsonFile) as pkmnFile:
        pkmnInformation = json.load(pkmnFile)
    linkText, outfilename, markdownText = pkmnWriter.getPokemonMarkdown(pkmnInformation)
    with open(docOutFolder+outfilename, mode='w') as outputMarkdown:
        outputMarkdown.write(markdownText)
    allLinkText+=linkText

with open(pokemonLinkTextFile, mode = 'w') as plFile:
    plFile.write(allLinkText)