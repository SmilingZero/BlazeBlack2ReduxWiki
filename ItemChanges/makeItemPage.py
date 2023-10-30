import os
import re
from collections import OrderedDict

imageFolder = 'docs/img/items'
itemImageFiles = os.listdir(imageFolder)
imFileKeys = {''.join(filter(str.isalnum, i.replace('.png', ''))).lower().replace('é', 'e') : i for i in itemImageFiles}

# This is to streamline the creation of many of the tables for the item page...
outFile = 'ItemChanges/out_modifiedItems.txt'
with open('ItemChanges/modifiedItems.txt', mode = 'r') as doc:
    rawChanges = doc.read();

def getMatchingImageFile(itemname):
    matchstr = ''.join(filter(str.isalnum, itemname)).lower().replace('é', 'e')
    imFile = imFileKeys[matchstr]
    tableString = '![][{s}]'.format(s=matchstr)
    inclString = '[{s}]: img/items/{f}'.format(s = matchstr, f = imFile)
    return tableString, inclString

outString = ''
inclString = ''


secs = rawChanges.split('\n\n')

replacedItems = secs[0].splitlines()
replacedItems = [l for l in replacedItems if l]
replacedItemsString = replacedItems[0]+'\n\n'
replacedItemsContent = replacedItems[1:]
replacedItemsHeaders = ['__Old Item__ <br> __Unavailable__', '__New Item__']
replacedItemsTable = '| ' + ' | '.join(replacedItemsHeaders) + ' |\n'
replacedItemsTable += '|: ' + ' :|: '.join(['---']*len(replacedItemsHeaders)) + ' :|\n'

def getReplaceRow(line):
    contentReg = re.compile('- (.+) -> (.+)')
    return '| ' + ' | '.join(re.findall(contentReg, line)[0]) + ' |'
replacedItemsTable += '\n'.join([getReplaceRow(l) for l in replacedItemsContent])+'\n'
replacedItemsString += replacedItemsTable

costAdj = [i for i in secs[1].splitlines() if i]
costAdjString = costAdj[0]+'\n\n'
costAdjContent = costAdj[1:]
costHeaders = ['__Item__', '__Old Price__', '__New Price__']
costTable = '| ' + ' | '.join(costHeaders) + ' |\n'
costTable += '|: ' + ' :|: '.join(['---']*len(costHeaders)) + ' :|\n'

def getCostRow(line):
    costReg = re.compile('- (.+) \((.+)-> (.+)\)')
    raw = re.findall(costReg, line)
    raw = [i.strip() for i in raw[0]]
    tblImString, inclString = getMatchingImageFile(raw[0])
    content = raw
    content[0] = '{image}<br>{name}'.format(image = tblImString, name = raw[0])
    tblString = '| ' + ' | '.join(content) + ' |'
    return tblString, inclString
costTableRows = [getCostRow(i) for i in costAdjContent]
costTable+= '\n'.join([i[0] for i in costTableRows]) + '\n'
inclString += '\n'.join([i[1] for i in costTableRows]) + '\n'
costAdjString+=costTable

newUseItems = [i for i in secs[2].splitlines() if i]
newUseString = newUseItems[0]+'\n\n'
newHeaders = ['&nbsp;', 'Item']
newUseString+= '| ' + ' | '.join(newHeaders) + ' |\n' + '|: ' + ' :|: '.join(['---']*len(newHeaders)) + ' :|\n'
newUse = newUseItems[1:]

def getNewItemRow(line):
    reg = re.compile('- (.+)')
    raw = re.findall(reg, line)[0].strip()
    tblImString, inclString = getMatchingImageFile(raw)
    return '| ' + ' | '.join([tblImString, raw]) + ' |', inclString


rows = [getNewItemRow(i) for i in newUse]
newUseString += '\n'.join([i[0] for i in rows]) + '\n'
inclString +='\n'.join([i[1] for i in rows]) + '\n'


inclString = "\n".join(list(OrderedDict.fromkeys(inclString.split("\n"))))

outString += '\n\n'.join([replacedItemsString, costAdjString, newUseString]) + '\n\n\n\n' + inclString

with open(outFile, mode = 'w') as f:
    f.write(outString)

