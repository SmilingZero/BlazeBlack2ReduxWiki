import csv
import re
import os


pokemonIndexFile = './data/pokemonIndexList.csv'
with open(pokemonIndexFile, 'r', encoding='utf-8-sig') as indexFile:
    reader = csv.reader(indexFile)
    pokemonNumberMap = { row[2]: int(row[1]) for row in reader}

linebreak = re.compile('(\n[0-9])')

itemFileNames = os.listdir('docs/img/items')
itemImageNames = [os.path.splitext(filename)[0] for filename in itemFileNames]
# ''.join(filter(str.isalpha, s))

def getMatchingItemFile(item):
    lowerAlphaItem = ''.join(filter(str.isalpha, item.lower()))
    matchingFile = [i for i in itemFileNames if ''.join(filter(str.isalpha, os.path.splitext(i)[0].lower())) == lowerAlphaItem]
    return matchingFile[0]

with open('evolChange.txt', mode='r') as evol:
    filetext = evol.read()
    linebreaks = [m.start(0) for m in re.finditer(linebreak, filetext)]
    linebreaks.insert(0,0)
    linebreaks.append(len(filetext))
    entries = [filetext[linebreaks[i]:linebreaks[i+1]] for i in range(len(linebreaks)-1)]
    title = '| ' + ' | '.join(['Pokémon', 'New Method', 'Evolution']) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*3) + ' :|\n'
    inclString = ''
    tableText = title+separator
    for entry in entries:
        lines = entry.split('\n')
        lines = [i for i in lines if i]
        thisMon = lines[0][0:19].strip()
        nextMons = [i[20:].strip() for i in lines]
        num = thisMon[0:3]
        thisName = thisMon[3:].strip()
        col1 = '![][{num}]<br>#{num}<br>[{name}]'.format(num=num, name=thisName)
        inclString+= '[{name}]: pokemons/{num}/ \n [{num}]: img/pokemon/{stripNum}_0.png \n'\
                                            .format(num=num, name=thisName, stripNum=str(int(num)))
        for evo in nextMons:
            exp = re.findall('Now evolves into ([\S]+) (.+)', evo)
            nextName = exp[0][0]
            method = exp[0][1]
            if 'Mime' in thisMon:
                nextName = 'Mr. Mime'
                method = 'at Level 25.'
            
            nextNum = "{0:03}".format(pokemonNumberMap[nextName])
            col3 = '![][{num}]<br>#{num}<br>[{name}]'.format(num=nextNum, name=nextName)
            inclString+= '[{name}]: pokemons/{num}/ \n [{num}]: img/pokemon/{stripNum}_0.png \n'\
                                            .format(num=nextNum, name=nextName, stripNum=str(int(nextNum)))
            
            if 'at Level' in method or 'is in the party' in method:
                col2 = method
            elif 'via the use of' in method:
                item = re.findall('via the use of (?:an|a) (.+).', method)[0]
                lowerAlphaItem = ''.join(filter(str.isalpha, item.lower()))
                itemFile = getMatchingItemFile(item)
                col2 = '![][{itemStr}]<br>{item}'.format(itemStr=lowerAlphaItem, item=item)
                inclString+= '[{itemstr}]: img/items/{file} \n'.format(itemstr=lowerAlphaItem, file=itemFile)
            elif 'friendship' in method:
                col2 = 'Friendship At Any Time of Day'
            elif 'while knowing the move' in method:
                move = re.findall('by leveling up while knowing the move (.+).', method)[0]
                col2 = 'Level Up While Knowing {move}'.format(move=move)
            else:
                vwev =1
            tableText+= '| ' + ' | '.join([col1,col2,col3]) + ' |\n'
    with open('evolTable.txt', mode = 'w') as outFile:
        outFile.write(tableText+'\n\n'+inclString)