import csv

legendaryMons = [144,
145,
146,
150,
151,
243,
244,
245,
249,
250,
251,
377,
378,
379,
380,
381,
382,
383,
384,
385,
386,
480,
481,
482,
483,
484,
487,
493,
485,
486,
488,
491,
490,
489,
492,
494,
638,
639,
640,
641,
642,
645,
644,
643,
646,
647,
648,
649]

pokemonIndexFile = './data/pokemonIndexList.csv'
with open(pokemonIndexFile, 'r', encoding='utf-8-sig') as indexFile:
    reader = csv.reader(indexFile)
    pokemonNumberMap = { int(row[1]): row[2] for row in reader}



outContent = ["[{name}]: pokemons/{str}/".format(name=pokemonNumberMap[i], str = f"{int(i):03}") for i in legendaryMons]
'\n'.join(outContent)
with open('tmp.txt', mode='w') as tt:
    tt.write('\n'.join(outContent))
