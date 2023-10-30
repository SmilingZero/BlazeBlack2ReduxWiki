infile = 'ItemChanges/tmChange.txt'
outfile = 'ItemChanges/out_tmChange.txt'

pipeInsertPoints = [0, 6 ,39] #also at the end
with open(infile, 'r') as f:
    rawTable = f.read()
    rawRows = rawTable.splitlines()
    rowsWithPipes = ['| '+l[0:6] +'|'+ l[6:39] + '|'+l[39:] +' |' for l in rawRows]    
    rowsWithPipes[1] = '|: '+rawRows[1][0:6] +':|:'+ rawRows[1][6:39] + '|:'+rawRows[1][39:] +' |'
    with open(outfile, 'w') as h:
        h.write('\n'.join(rowsWithPipes) + '\n')
