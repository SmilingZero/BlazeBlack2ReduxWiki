import re

dataFile = 'one-off/moveChangeList.txt'
with open(dataFile, mode = 'r') as f:
    moveChangesString = f.read()

sectionReg = re.compile('={2,}\n(.+)\n={2,}')

strt = [m.start(0) for m in re.finditer(sectionReg, moveChangesString)]
strt.insert(0,0)
strt.append(len(moveChangesString))
moveSections = [moveChangesString[strt[i]:strt[i+1]] for i in range(0, len(strt)-1) if moveChangesString[strt[i]:strt[i+1]]]
tableTexts = ''
for ind, sec in enumerate(moveSections):
    splitSec = sec.split('\n\n')
    title = re.findall(sectionReg, splitSec[0])[0] # should be ## level

    entries = [splitSec[i] for i in range(1,len(splitSec)) if splitSec[i]]
    # entry should be table in ### section with movename as header

    def makeSubsection(entry):
        colNames = ['&nbsp;', 'Old', 'New']
        lines = entry.split('\n')
        subsection = '### {name}\n\n'.format(name=lines[0])
        subsection += '| ' + ' | '.join(colNames) + ' |\n'
        subsection += '|: ' + ' :|: '.join(['---']*len(colNames)) + ' :|\n'
        def makeRow(e):
            entryReg = re.compile('- ([A-z]+) (.+) -> (.+)')
            s = re.findall(entryReg, e)
            s = [i.strip() for i in s[0]]
            s = [i if i!='None' else '&nbsp' for i in s]
            row = '| ' + ' | '.join(s) + ' |'
            return row
        contentRows = [makeRow(e) for e in lines[1:]]
        subsection+= '\n'.join(contentRows)+'\n'
        return subsection
    processedEntries = [makeSubsection(e) for e in entries]
    sectionText = '## {name}\n\n'.format(name = title)
    sectionText+= '\n'.join(processedEntries)+'\n'
    tableTexts+=sectionText+'\n'

with open('outMoveTables.txt', mode = 'w') as f:
    f.write(tableTexts)