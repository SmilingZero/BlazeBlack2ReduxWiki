import os
import stat
import re
from collections import OrderedDict



outFile = 'ItemChanges/out_itemtable.txt'

imageFolder = 'docs/img/items'
itemImageFiles = os.listdir(imageFolder)
imFileKeys = {''.join(filter(str.isalnum, i.replace('.png', ''))).lower().replace('é', 'e') : i for i in itemImageFiles}

def getMatchingImageFile(itemname):
    matchstr = ''.join(filter(str.isalnum, itemname)).lower().replace('é', 'e')
    imFile = imFileKeys[matchstr]
    tableString = '![][{s}]'.format(s=matchstr)
    inclString = '[{s}]: img/items/{f}'.format(s = matchstr, f = imFile)
    return tableString, inclString

outString = ''
inclString = ''

locFile = 'ItemChanges/itemLocations.txt'

if os.stat(locFile)[stat.ST_SIZE] <= 0:
    raise Exception('Locations file does not exist')

with open('ItemChanges/itemLocations.txt', mode = 'r') as doc:
    rawLocations = doc.read();

locationReg = re.compile('~{2,} (.+) ~{2,}')
sectionStarts = [m.start(0) for m in re.finditer(locationReg,rawLocations)]
sectionStarts.append(len(rawLocations))
itemSections = [rawLocations[sectionStarts[i]:sectionStarts[i+1]] for i in range(len(sectionStarts)-1)]

def getLocationTable(sec):
    lines = [i for i in sec.splitlines() if i]
    headerLabels = ['__Old Item__', '__ New Item__']
    sectionTable = '| ' + ' | '.join(headerLabels) + ' |\n'
    sectionTable+= '|: ' + ' :|: '.join(['---']*len(headerLabels)) + ' :|\n'
    location = re.findall(locationReg, lines[0])[0]
    items = lines[1:]
    def getItems(line):
        line = line.strip()
        thisReg = re.compile('(.+)')
        hasArrow = False
        if '->' in line:
            hasArrow = True
            thisReg = re.compile('(.+)->') if '>' == line[-1] else re.compile('(.+)->(.+)')
        itemsInEntry = re.findall(thisReg, line)[0]
        if type(itemsInEntry) is not tuple:
            col1 = itemsInEntry.strip()
            col2 = 'None' if hasArrow else '&nbsp;'
        else:
            col1 = itemsInEntry[0].strip()
            col2 = itemsInEntry[1].strip()
        items = (col1, col2)
        return items

    itemEntries = [getItems(i) for i in items if len(i.replace(' ',''))>0]
    sectionTable += '\n'.join([
        '| ' + ' | '.join(i) +' |' for i in itemEntries
    ]) + '\n'
    sectionText = '### {loc}\n\n'.format(loc=location) + sectionTable
    return sectionText

sectables = [getLocationTable(i) for i in itemSections]
outString = '\n'.join(sectables)+'\n'
with open(outFile, 'w') as f:
    f.write(outString)

dve = 1