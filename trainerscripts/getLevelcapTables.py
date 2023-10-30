import re

levelcapList = 'trainerscripts/levelcap.txt'
challengeCapList = 'trainerscripts/levelcap_challenge.txt'
totalChallengeCapList = 'trainerscripts/total_levelcap_challenge.txt'


outText = 'trainerscripts/out_tables.txt'

def getSimpleList(textFile):
    reg = re.compile('- (.+), (.+)')
    with open(textFile, 'r') as f:
        rawText = f.read()
    lines = rawText.splitlines()
    lines = [i for i in lines if i]
    content = [re.findall(reg, i)[0] for i in lines]
    header = ['__Battle__', '__Level Cap__']
    tableString = '| ' + ' | '.join(header) + ' |\n'
    tableString += '| ' + ' | '.join(['---']*len(header)) + ' |\n'
    rows = '\n'.join(['| ' + ' | '.join(r) + ' |' for r in content])
    tableString+=rows
    return tableString

def getTotalList(textFile):
    reg = re.compile('(.+) ([0-9]{2}) (.+)')
    with open(textFile, 'r') as f:
        rawText = f.read()
    
    lines = rawText.splitlines()
    lines = [i for i in lines if i]
    content = [re.findall(reg, i)[0] for i in lines]

    header = ['__Required__','__Level Cap__','__Battle__']
    tableString = '| ' + ' | '.join(header) + ' |\n'
    tableString += '| ' + ' | '.join(['---']*len(header)) + ' |\n'
    rows = '\n'.join(['| ' + ' | '.join(r) + ' |' for r in content])
    tableString+=rows

    tableString = tableString.replace('●', ':exclamation:')
    tableString = tableString.replace('○', ':grey_exclamation:')
    tableString = tableString.replace('♕', ':warning:')
    tableString = tableString.replace('♛', ':warning:')
    return tableString


if __name__ == "__main__":
    normTable = getSimpleList(levelcapList)
    challengeTable = getSimpleList(challengeCapList)
    totalTable = getTotalList(totalChallengeCapList)
    with open(outText, 'w') as f:
        f.write('\n\n\n'.join([normTable, challengeTable, totalTable]))