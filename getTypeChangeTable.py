import csv
import re
import os


# pokemonIndexFile = './data/pokemonIndexList.csv'
# with open(pokemonIndexFile, 'r', encoding='utf-8-sig') as indexFile:
#     reader = csv.reader(indexFile)
#     pokemonNumberMap = { row[2]: ow[2] for row in reader}

def getTypeIncludes():
    typesFolder = 'docs/img/type/'
    typeFiles = os.listdir(typesFolder)
    includeText = ''
    for i, fname in enumerate(typeFiles):
        typestring = fname.replace('.png', '')
        typeInclude = "[{type}]: img/type/{fid}\n".format(type=typestring, fid=fname)
        includeText += typeInclude
    return includeText



typeDocRegex = re.compile('#([0-9]+) ([A-z\']+) {2,} ([\S]+ \/ [\S]+|[\S]+) {2,} ([\S]+ \/ [\S]+|[\S]+) {2,} (.+)')
fileText = ''
with open('typechange.txt', mode = 'r') as typechangefile:
    tmp = typechangefile.read().split('\n')
    typeChangeStrings = tmp[2:]
    typeChangeData = [ re.findall(typeDocRegex,str)[0] for str in typeChangeStrings]
    tableText = '| ' + ' | '.join(['Pokémon', 'Old Type', 'New Type', 'Justification']) + ' |\n'
    tableText += '|: ' + ' :|: '.join(['---']*4) + ' :|\n'
    inclString = ''
    for ind, set in enumerate(typeChangeData):
        rowContent = ['![][{num}]<br>#{num} [{name}]'.format(num=set[0], name=set[1])]
        typeCells = ['<br>'.join(['![][{t}]'.format(t=type.strip().lower())  for type in set[i].split('/')]) for i in [2, 3]]
        [rowContent.append(s) for s in typeCells]
        rowContent.append(set[4])
        inclString += '[{name}]: pokemons/{num}/ \n [{num}]: img/pokemon/{stripNum}_0.png \n'\
                                            .format(num=set[0], name=set[1], stripNum=str(int(set[0])))
        tableText += '| ' + ' | '.join(rowContent) + ' |\n'
    inclString+= getTypeIncludes()
    fileText += tableText +'\n\n' + inclString
with open('typechangestable.txt', mode = 'w') as typechangefile:
    typechangefile.write(fileText);
sdvwevwev = 1