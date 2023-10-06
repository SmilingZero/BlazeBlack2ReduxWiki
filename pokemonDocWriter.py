from genericpath import isfile
import os
import tqdm
import json
import csv
import re

def getTypeIncludes():
    typesFolder = 'docs/img/type/'
    typeFiles = os.listdir(typesFolder)
    includeText = ''
    for i, fname in enumerate(typeFiles):
        typestring = fname.replace('.png', '')
        typeInclude = "[{type}]: ../img/type/{fid}\n".format(type=typestring, fid=fname)
        includeText += typeInclude
    return includeText

def getSpeciesTypeString(typeList):
    individualTypeStrings = ['![][{typename}]'.format(typename=s.lower()) for s in typeList]
    return ' '.join(individualTypeStrings)

def getTopLevelHeader(pkmnInformation):
    number = pkmnInformation[0]['Number']
    natDexNumber = f"{number:03}"
    speciesName = pkmnInformation[0]['Name']
    formMarkerInd = speciesName.find('-')
    speciesTypeString = getSpeciesTypeString(pkmnInformation[0]['TYPE'])
    
    if formMarkerInd != -1:
        speciesName = speciesName[:formMarkerInd].strip()
    if len(pkmnInformation) > 1:
        headerText = "# {number} - {speciesname}\n".format(number = natDexNumber, speciesname = speciesName)
    else:
        headerText = "# {number} - {speciesname} &nbsp; {type}\n".format(number = natDexNumber, speciesname = speciesName, type=speciesTypeString)
    return headerText


def getPokemonMarkdown(pkmnInformation):
    # Regardless of number of forms, the natDex number is constant...
    number = pkmnInformation[0]['Number']
    natDexNumber = f"{number:03}"
    topLevelHeader = getTopLevelHeader(pkmnInformation)
    if len(pkmnInformation) > 1:
        print('Have not implemented')
    else:
        bodyText = getSingleFormMarkdown(pkmnInformation[0])

    markdownText = topLevelHeader + bodyText + getTypeIncludes()
    outfilename = natDexNumber+'.md'
    return outfilename, markdownText

def getTypeTable(defense):
    markdownTable = '## Defenses\n'
    tableHeader = '\n| ' + ' | '.join(defense.keys()) + ' |\n'
    separator = '| ' + ' | '.join(['---' for i in defense.keys()]) + ' |\n'
    def getCol(v):
        if len(v) == 0:
            return '&nbsp;'
        else:
            return '<br>'.join(['![][{type}]'.format(type = i.lower()) for i in v])+'<br>'
    contentRow = '| ' + ' | '.join([getCol(v) for k,v in defense.items()]) + ' |\n'
    return markdownTable+tableHeader+separator+contentRow+'\n'

def getSingleFormMarkdown(pkmnInformation):
    number = pkmnInformation['Number']
    natDexNumber = f"{number:03}"
    pkmnInclude, imString = getPokemonImage(number,0)

    bodyText = ''
    bodyText+=imString
    bodyText+= getTypeTable(pkmnInformation['Defenses'])
    bodyText+=pkmnInclude
    return bodyText

def getPokemonImage(number, form):
    natDexNumber = f"{number:03}"
    imString = "![][{nm}]\n".format(nm=natDexNumber)
    fname = str(number)+'_'+str(form)+'.png'
    pkmnInclude = "[{nm}]: ../img/pokemon/{fid}\n".format(nm=natDexNumber, fid=fname)
    return pkmnInclude, imString
    