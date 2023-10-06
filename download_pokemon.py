
from genericpath import isfile
from os import makedirs
import requests
import tqdm

makedirs("temp/pokemon/",exist_ok=True)
makedirs("temp/ability/",exist_ok=True)
makedirs("temp/move/",exist_ok=True)
makedirs("temp/item/",exist_ok=True)

pokemonIndices = [i for i in range(1,650)]
otherFormsIndices = [i for i in range(10001, 10025)]
[pokemonIndices.append(i) for i in otherFormsIndices]
for id in tqdm.tqdm(pokemonIndices):

    if isfile(f"temp/pokemon/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")

    if response == "Not Found":
        continue

    fh = open(f"temp/pokemon/{id}.json", "wb")
    fh.write(response.content)
    fh.close()

for id in tqdm.tqdm(range(1, 165)):

    if isfile(f"temp/ability/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/ability/{id}")

    if response == "Not Found":
        continue

    fh = open(f"temp/ability/{id}.json", "wb")
    fh.write(response.content)
    fh.close()

for id in tqdm.tqdm(range(1, 851)):

    if isfile(f"temp/move/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/move/{id}")

    if response == "Not Found":
        continue

    fh = open(f"temp/move/{id}.json", "wb")
    fh.write(response.content)
    fh.close()

for id in tqdm.tqdm(range(1,1607)):

    if isfile(f"temp/item/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/item/{id}")

    if response == "Not Found":
        continue

    fh = open(f"temp/item/{id}.json", "wb")
    fh.write(response.content)
    fh.close()