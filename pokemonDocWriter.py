import os
import json
import csv
from collections import OrderedDict
from difflib import SequenceMatcher
import re
import pickle
import networkx as nx
import itertools
import copy

# image_base_link = 'https://smilingzero.github.io/BlazeBlack2ReduxWiki/img/animated/'
# pokemon_base_link = 'https://smilingzero.github.io/BlazeBlack2ReduxWiki/pokemons/'


image_base_link = '../../img/animated/'
pokemon_base_link = '../'


def unnest(d, keys=[]):
    result = []
    for k, v in d.items():
        if isinstance(v, dict):
            result.extend(unnest(v, keys + [k]))
        else:
            result.append(tuple(keys + [k, v]))
    return result

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
pokemonImageLookup = './data/speciesImageLookup.json'
with open(pokemonImageLookup, 'r') as f:
    speciesImageLookup = json.load(f)
pokemonIndexFile = './data/pokemonIndexList.csv'
with open(pokemonIndexFile, 'r', encoding='utf-8-sig') as indexFile:
    reader = csv.reader(indexFile)
    pokemonNumberMap = { row[2]: f"{int(row[1]):03}" for row in reader}
detailedMoveListFile = 'scrapedJSON/ref/moves_with_descriptions.json'
with open(detailedMoveListFile) as f:
    detailedMoveList = json.load(f)
pokemonEncounterLocations = 'scrapedJSON/ref/pokemonEncounters.json'
with open(pokemonEncounterLocations) as f:
    pokemonEncounters = json.load(f)
with open('locationLinkDict.json', mode = 'r') as f:
    locationLinks = json.load(f)
with open('scrapedJSON/ref/evo_branches.pickle', mode = 'rb') as f:
    evo_branches = pickle.load(f)
    
def getTopLevelHeader(pkmnInformation):
    number = pkmnInformation['Number']
    natDexNumber = f"{number:03}"
    mon = pkmnInformation['Name']
    speciesName = pkmnInformation['Name']
    if'♂' in mon or mon.lower() == 'nidoran-m':
        speciesName= 'Nidoran♂'
    elif '♀' in mon or mon.lower() == 'nidoran-f':
        speciesName= 'Nidoran♀'
    formMarkerInd = speciesName.find('-')
    if formMarkerInd != -1 and speciesName != 'Ho-Oh':
        speciesName = speciesName[:formMarkerInd].strip()
    
    headerText = "{number} - {speciesname}".format(number = natDexNumber, speciesname = speciesName)
    return headerText

def getSpecies(mon):
    hyphenInd = mon.find('-')
    if'♂' in mon or mon.lower() == 'nidoran-m':
        form = 'base' 
        species= 'nidoranu2642'
    elif '♀' in mon or mon.lower() == 'nidoran-f':
        form = 'base'
        species= 'nidoranu2640'
    elif 'Porygon-Z' == mon:
        form = 'base'
        species = 'porygonz'
    elif 'Ho-Oh' == mon:
        species = 'hooh'
        form = 'base'
    else:
        if hyphenInd == -1:
            form = 'base'
            species = mon.lower().strip()
        else:
            form = mon[hyphenInd+1:].strip().lower()
            species = mon[:hyphenInd].strip().lower()
        species = "".join([ c if c.isalnum() else "" for c in species ])
    return species, form

def getPokemonImageHTML(name, form, size = None):
    name_key = name
    if name == 'nidoran':
        if form == 'f':
            name_key = 'nidoranu2640'
            form = 'base'
        elif form == 'm':
            name_key = 'nidoranu2642'
            form = 'base'
        else:
            raise ValueError
    num = speciesImageLookup[name_key.lower()]['NatDexNum']
    fname = speciesImageLookup[name_key.lower()][form]
    natDexNumber = f"{num:03}"
    out_string = "<img src=\"../../img/animated/{fid}\">".format(nm=natDexNumber, f = form, fid=fname)
    if size is not None:
        out_string = out_string = "<img src=\"../../img/animated/{fid}\" width=\"{size}\">".format(nm=natDexNumber, f = form, fid=fname, size = size)
    return out_string

def getStatEntry(data):
    stats = data['STATS']
    if 'VANILLA STATS' in data:
        vanilla_stats = data['VANILLA STATS']
        stat_diff = { k: stats[k]-vanilla_stats[k] for k in stats.keys()}
    else:
        stat_diff = { 0 for k in stats.keys()}
    cols = [i for i in stats.keys()]
    cols.append('BST')
    def get_header(t,d,w):
        if d == 0:
            # return f"<th class=\"stat\" style=\"width:{w}%;align:center;vertical-align: middle;\">{t}</th>"
            return f"<th class=\"stat\">{t}</th>"
        if d > 0:
            s_diff_tag = 'sup'
            s_color = 'green'
            d = '+' + str(d)
        else:
            s_diff_tag = 'sub'
            s_color = 'red'
        # return f"<th  class=\"stat\" style=\"width:{w}%;align:center;vertical-align: middle;color:{s_color};\">{t}<{s_diff_tag} style = \"line-height:0px;vertical-align: 5px;font-size: 10px;color:{s_color}\">{d}</{s_diff_tag}></th>"
        return f"<th  class=\"stat\" style=\"color:{s_color};\">{t}<{s_diff_tag} style = \"line-height:0px;vertical-align: 5px;font-size: 10px;color:{s_color}\">{d}</{s_diff_tag}></th>"
    
    def getContentString(s,w):
        # return f"<td class=\"stat\" style=\"width:{w}%;align:center;vertical-align: bottom;\">{s}</td>"
        return f"<td class=\"stat\">{s}</td>"
    
    content = [v for i,v in enumerate(stats.values())]
    content.append(sum(content))
    diff = [v for i,v in enumerate(stat_diff.values())]
    diff.append(sum(diff))
    width = [14, 14, 14, 14, 14, 14, 16]
    html_headers = [get_header(cols[t], diff[t], width[t]) for t in range(len(cols))]
    html_content = [getContentString(content[i],width[i]) for i in range(len(content))]
    return html_headers, html_content

def getStatTable(data):
    table_contents = []
    if len(data) == -1:
        data = data[0]
        html_headers, html_content = getStatEntry(data)
        header_row = "<tr>{h}</tr>".format(h=''.join(html_headers))
        content_row = "<tr>{h}</tr>".format(h=''.join(html_content))
        table_contents.append(header_row+'\n'+content_row)
    else:
        for d in data:
            _html_headers, _html_content = getStatEntry(d)
            name = d['Name']
            _imString = []
            for n in name:
                species, form = getSpecies(n)
                _imString.append(getPokemonImageHTML(species,form, 25))
            imString = ''.join(_imString)
            _html_headers.insert(0,"<th class=\"stat-icon\" rowspan=\"2\">{c}</th>".format(c=imString))
            header_row = "<tr>{h}</tr>".format(h=''.join(_html_headers))
            content_row = "<tr>{h}</tr>".format(h=''.join(_html_content))
            table_contents.append(header_row+'\n'+content_row)

    table_string = '<table class=\"stat\">{body}</table>\n\n'.format(body = '\n'.join(table_contents))
    return table_string

def getStatEntry_Single(data):
    stats = data['STATS']
    if 'VANILLA STATS' in data:
        vanilla_stats = data['VANILLA STATS']
        stat_diff = { k: stats[k]-vanilla_stats[k] for k in stats.keys()}
    else:
        stat_diff = { 0 for k in stats.keys()}
    cols = [i for i in stats.keys()]
    cols.append('BST')
    def getCell(title, diff, value):
        if diff == 0:
            return "<td class=\"stat-single\"><span style=\"font-weight:700;\"><u>{ti}</u></span><br>{val}</td>".format(ti = title, val = value)
        if diff > 0:
            s_diff_tag = 'sup'
            s_color = 'green'
            diff = '+' + str(diff)
        else:
            s_diff_tag = 'sub'
            s_color = 'red'
        return "<td  class=\"stat-single\">\
            <u><span style=\"font-weight:700; color:{s_color};\">{ti}</span>\
                <{s_diff_tag} style = \"line-height:0px;vertical-align: 5px;font-size: 10px;color:{s_color}\">{di}</{s_diff_tag}></u>\
                    <br>{val}</td>".format(s_color = s_color, ti = title, \
                                           s_diff_tag=s_diff_tag, di = diff, val = value)
        
    content = [v for i,v in enumerate(stats.values())]
    content.append(sum(content))
    diff = [v for i,v in enumerate(stat_diff.values())]
    diff.append(sum(diff))

    html_cells = [getCell(cols[t], diff[t], content[t]) for t in range(len(cols))]
    return html_cells

def getStatTable_JointColumns(data):
    table_contents = []
    for d in data:
        _html_content = getStatEntry_Single(d)
        name = d['Name']
        _imString = []
        for n in name:
            species, form = getSpecies(n)
            _imString.append(getPokemonImageHTML(species,form, 25))
        imString = ''.join(_imString)
        _html_content.insert(0,"<td class=\"stat-icon-single\">{c}</td>".format(c=imString))
        content_row = "<tr>{h}</tr>".format(h=''.join(_html_content))
        table_contents.append(content_row)
    table_string = '<table class=\"stat\">{body}</table>\n\n'.format(body = '\n'.join(table_contents))
    return table_string

def getItemString(itemList):
    content = ['- {i}%: {j}'.format(i = item[0], j = item[1]) for item in itemList.items()]
    return '\n'.join(content)+'\n'

def getMoveData(movename):
    return [i for i in detailedMoveList if i['Name'].lower().replace(' ', '') == movename.lower().replace(' ', '')][0]

def getPokemonSpriteCell(name):
    _imString = []
    for n in name:
        species, form = getSpecies(n)
        _imString.append(getPokemonImageHTML(species,form, 25))
    imString = ''.join(_imString)
    return f'<td>{imString}</td>'

def getMoveContent(move_data):
    ['Name', 'Power', 'Accuracy', 'PP' ,'Type', 'Damage Class', 'Effect']
    content = ['<td>{c}</td>'.format(c=move_data[k]) for k in ['Name', 'Power', 'Accuracy', 'PP']]
    content.append(\
        '<td><img src=\"../../img/type/{type}.png\"></td>'.format(type = move_data['Type'].lower())\
    )
    content.append(\
        '<td><img src=\"../../img/type/{type}.png\"></td>'.format(type = move_data['Damage Class'].lower())\
    )
    content.append(\
        '<td>Priority: {prio}. {effect}</td>'.format(\
            prio = move_data['Priority'], effect = str(move_data['Effect']).replace('\n', '<br>'))\
    )
    return ''.join(content)

def getLevelUpTableWithForms(data):
    tableColumns = ['Level', 'Name', 'Power', 'Accuracy', 'PP' ,'Type', 'Damage Class', 'Effect']
    if len(data)>1:
        tableColumns.insert(0, 'Form')
    all_moves = []
    for d in data:
        _moves = d['Level Up Moves']
        [m.update({'Name':d['Name']}) for m in _moves]
        _t_moves = [[v for k,v in m.items()] for m in _moves]
        all_moves.extend(_t_moves)
    all_moves.sort()
    _grouped_move = [[list(u), [vv[2] for vv in v]] for u,v in itertools.groupby(all_moves, key=lambda x: (x[0], x[1]))]
    grouped_move = [[_g[0][0], _g[0][1], [g for gs in _g[1] for g in gs]] for _g in _grouped_move]
    grouped_move_data = [[g[0], getMoveData(g[1]), g[2]] for g in grouped_move]
    def getLevelColumn(lvl):
        return f'<td>{lvl}</td>'
    if len(data) > 1:
        _move_content = [ [getPokemonSpriteCell(g[2]), getLevelColumn(g[0]), getMoveContent(g[1])] for g in grouped_move_data]
    else:
         _move_content = [ [getLevelColumn(g[0]), getMoveContent(g[1])] for g in grouped_move_data]
    move_content = ['<tr>{r}</tr>'.format(r = ''.join(_m)) for _m in _move_content]
    table_body = '\n'.join(move_content)
    html_header = ''.join(['<th>{h}</th>'.format(h = h) for h in tableColumns])
    level_table = f'<table>{html_header}\n{table_body}\n</table>'
    return level_table

def getTMTableWithForms(data):
    tableColumns = ['Machine', 'Name', 'Power', 'Accuracy', 'PP' ,'Type', 'Damage Class', 'Effect']
    if len(data)>1:
        tableColumns.insert(0, 'Form')
    all_moves = []
    for d in data:
        _moves = d['TM Moves']
        [m.update({'Name':d['Name']}) for m in _moves]
        _t_moves = [[v for k,v in m.items()] for m in _moves]
        all_moves.extend(_t_moves)
    _tm = [_m for _m in all_moves if 't' in _m[0].lower()]
    _hm = [_m for _m in all_moves if 'h' in _m[0].lower()]
    def machineSort(m):
        return int(m.lower().replace('tm','').replace('hm',''))
    sortTM = sorted(_tm, key = lambda d: machineSort(d[0]))
    _grouped_tm = [[list(u), [vv[1] for vv in v]] for u,v in itertools.groupby(sortTM, key=lambda x: (x[0], x[2]))]
    grouped_tm = [[_g[0][0], _g[0][1], [g for gs in _g[1] for g in gs]] for _g in _grouped_tm]
    sortHM = sorted(_hm, key = lambda d: machineSort(d[0]))
    _grouped_hm = [[list(u), [vv[1] for vv in v]] for u,v in itertools.groupby(sortHM, key=lambda x: (x[0], x[2]))]
    grouped_hm = [[_g[0][0], _g[0][1], [g[0] for g in _g[1]]] for _g in _grouped_hm]
    grouped_move = grouped_tm
    grouped_move.extend(grouped_hm)
    grouped_move_data = [[g[0], getMoveData(g[1]), g[2]] for g in grouped_move]
    def getMachineColumn(m):
        return f'<td>{m}</td>'
    if len(data) > 1:
        _move_content = [ [getPokemonSpriteCell(g[2]), getMachineColumn(g[0]), getMoveContent(g[1])] for g in grouped_move_data]
    else:
         _move_content = [ [getMachineColumn(g[0]), getMoveContent(g[1])] for g in grouped_move_data]
    move_content = ['<tr>{r}</tr>'.format(r = ''.join(_m)) for _m in _move_content]
    table_body = '\n'.join(move_content)
    html_header = ''.join(['<th>{h}</th>'.format(h = h) for h in tableColumns])
    tm_table = f'<table>{html_header}\n{table_body}\n</table>'
    return tm_table

def getTutorTableWithForms(data):
    tableColumns = ['Name', 'Power', 'Accuracy', 'PP' ,'Type', 'Damage Class','Effect']
    if len(data) > 1:
        tableColumns.insert(0, 'Form')
    all_moves = []
    for d in data:
        _m = [[m, d['Name']] for m in d['Tutor Moves']]
        all_moves.extend(_m)
    all_moves.sort()
    _grouped_move = [[u, [vv[1] for vv in v]] for u,v in itertools.groupby(all_moves, key=lambda x: (x[0]))]
    grouped_move_data = [[g[1], getMoveData(g[0])] for g in _grouped_move]
    if len(data) > 1:
        _move_content = [ [getPokemonSpriteCell(g[0]), getMoveContent(g[1])] for g in grouped_move_data]
    else:
         _move_content = [ getMoveContent(g[1]) for g in grouped_move_data]
    move_content = ['<tr>{r}</tr>'.format(r = ''.join(_m)) for _m in _move_content]
    table_body = '\n'.join(move_content)
    html_header = ''.join(['<th>{h}</th>'.format(h = h) for h in tableColumns])
    tutor_table = f'<table>{html_header}\n{table_body}\n</table>'
    return tutor_table

def getPreEvoMoveSection(moveList):
    tableColumns = ['Species', 'Method', 'Move']
    tableHeader = '| ' + ' | '.join(tableColumns) + ' |\n'
    separator = '|: ' + ' :|: '.join(['---']*len(tableColumns)) + ' :|\n'
    def makeRow(entry):
        row = '| {species} | {method} | {move} |'.format(species = entry[0], method = entry[1], move = entry[2])
        return row
    contentRows = [makeRow(data) for data in moveList]
    return tableHeader+separator+'\n'.join(contentRows) +'\n\n'

def getEncounters(species):
    if(species != 'Ho-Oh' and '-' in species):
        formInd = species.find('-')
        species = species[:formInd].strip()
    def getSpeciesFromKey(k):
        formInd = k.find('-')
        if formInd !=-1:
            return k[:formInd].strip()
        return k
    wildEncounterKeys = [key for key in pokemonEncounters.keys() if species.lower() == getSpeciesFromKey(key).lower()]
    if len(wildEncounterKeys) == 0:
        return '',''
    def getForm(k):
        formInd = k.find('-')
        if formInd !=1:
            return k[formInd+1:].strip()
        return None
    encounterList = []
    if(len(wildEncounterKeys))>1:
        pokemonEncountersSubset = { getForm(k):pokemonEncounters[k] for k in wildEncounterKeys}
    else:
        pokemonEncountersSubset = pokemonEncounters[wildEncounterKeys[0]]
    def getPlaceLinkText(place):
        return '[{name}]'.format(name = place)
    def getPlaceLinkIncl(place):
        locationLinkKeys = list(locationLinks.keys())
        keysInPlace = [i for i in locationLinkKeys if i in place]
        locationSimilarity = [similar(place.lower(), i.lower()) for i  in keysInPlace]
        maxIndex = locationSimilarity.index(max(locationSimilarity))
        mostSimilarLocation = keysInPlace[maxIndex]
        # print(place, ',',mostSimilarLocation)
        return '[{name}]: ../../wildareas/{fname}'.format(name = place, fname = locationLinks[mostSimilarLocation].replace('.md', '/'))
    placeInclude = []
    unnested_encounters = unnest(pokemonEncountersSubset)
    unnested_encounters.sort(key = lambda item: tuple(i for i in item))
    if len(wildEncounterKeys) > 1:
        for row in unnested_encounters:
            form = row[0]
            location = row[1]
            data = row[-1]
            remaining_row = list(row)
            [remaining_row.pop(i) for i in [-1, 1, 0]]
            add_list = [[form, getPlaceLinkText(location), *remaining_row,e['Level'], round(e['Spawn Percent'],2)] for e in data]
            encounterList.extend(add_list)
            placeInclude.append(getPlaceLinkIncl(location))
    else:
        for row in unnested_encounters:
            data = row[-1]
            location = row[0]
            remaining_row = list(row)
            remaining_row.pop(0)
            remaining_row.pop(-1)
            add_list = [[getPlaceLinkText(location), *remaining_row,e['Level'], round(e['Spawn Percent'],2)] for e in data]
            encounterList.extend(add_list)
            placeInclude.append(getPlaceLinkIncl(location))
    placeInclude = '\n'.join(list(set(placeInclude)))
    n_cols = [len(e) for e in encounterList]
    max_cols = max(n_cols)
    colNames = ['&nbsp;']*max_cols
    colNames[-2] = 'Level'
    colNames[-1] = 'Spawn Percent'
    colNames[0] = 'Location'
    if len(wildEncounterKeys) > 1:
        colNames[0] = 'Form'
        colNames[1] = 'Location'
    
    adjusted_encounter_list = []
    for row in encounterList:
        this_length = len(row)
        missing_cols = max_cols - this_length
        row_list = list(row)
        [row_list.insert(-2,'&nbsp;') for i in range(missing_cols)]
        adjusted_encounter_list.append(row_list)
    topRow = '| ' + ' | '.join(colNames) + ' |\n'
    separator = '|: ' + ' :|: '.join(['--']*len(colNames)) + ' :|\n'
    content = ['| ' + ' | '.join([str(i) for i in row])  + ' |\n' for row in adjusted_encounter_list]
    tableString = topRow + separator + ''.join(content)
    return placeInclude,tableString

def isValid(item):
    if(item is None):
        return False
    if type(item) is not int and len(item) == 0:
        return False
    return True

def getSubsectionHeader(pkmnName):
    speciesName = pkmnName
    formMarkerInd = speciesName.find('-')
    if formMarkerInd == -1:
        headerName = speciesName
    else:
        headerName = speciesName[formMarkerInd:].replace('-','').strip()
    return '## {n}\n\n'.format(n=headerName)

def recurse_tree_for_heights(d, start):    
    if len(d[start].keys()) > 0:
        l = sum([recurse_tree_for_heights(d, next) for next in d[start].keys()])
    else:
        l = 1
    return l

def getEvolutionData(species):
    try:
        evo_branch = [b for b in evo_branches if species in [n.lower() for n in b.nodes]][0]
    except:
        return -1
    if len(evo_branch.edges()) == 0:
        return -1
    
    stages = []
    start_node = [n for n,d in evo_branch.in_degree if d == 0][0]
    end_nodes = [n for n,d in evo_branch.out_degree if d == 0]
    d = nx.dfs_successors(evo_branch, start_node)
    height_dict = {}
    flat_dict = nx.to_dict_of_dicts(evo_branch)
    for k in flat_dict.keys():
        tt = recurse_tree_for_heights(flat_dict, k)
        height_dict[k] = tt
    max_path_length = max([len([p for p in nx.all_simple_edge_paths(evo_branch, start_node, fe)][0]) for fe in end_nodes])
    [stages.append([]) for i in range(0,max_path_length+1)]
    for final_evo in end_nodes:
        path = [p for p in nx.all_simple_edge_paths(evo_branch, start_node, final_evo)][0]        
        for c in range(0,max_path_length):
            if c < len(path):
                p = path[c]
                start = p[0]
                end = p[1]
                mons_in_stages = [[s[0] for s in g] for g in stages]
                if start not in mons_in_stages[c]:
                    stages[c].append((start, -1,height_dict[start]))
                if end not in mons_in_stages[c+1]:
                    stages[c+1].append((end,evo_branch.get_edge_data(start, end)['label'], height_dict[end]))
            else:
                stages[c+1].append(('','',1))
    return stages

def formatEvolutionRows(stages):
    row_content = [[getEvolutionTableHTML(cell) for cell in col] for col in stages]
    max_rows = max([len(c) for c in row_content])
    row_strings = []
    for r in range(0, max_rows):
        tmp = ''
        for c in row_content:
            if r < len(c):
                tmp+=c[r]
        row_strings.append(f"<tr>{tmp}</tr>")
    return row_strings

def getEvolutionTableHTML(cell):
    pkmn = cell[0]
    if pkmn == '':
        return ''
    method = cell[1]
    cell_height = cell[2]

    species, form = getSpecies(pkmn)
    thisMonImages = speciesImageLookup[species]
    thisMonIm = thisMonImages[form]
    threeDigitNum = "{0:03}".format(thisMonImages['NatDexNum'])
    imageLink = image_base_link + thisMonIm
    imageLinkText = "<img src=\"{i}\">".format(i = imageLink)
    pkmnLinkText = "<a href=\"{hyperlink}\">{link_text}</a>".format(link_text = pkmn, hyperlink = pokemon_base_link + threeDigitNum)
    mon_cell = f"<td rowspan=\"{cell_height}\"style=\"vertical-align: middle;\"> {imageLinkText} <br> {pkmnLinkText} </td>"
    if method == -1:
        return mon_cell
    method_cell = f"<td rowspan=\"{cell_height}\"style=\"vertical-align: middle; word-break:break-all;\">{method}</td>"
    return method_cell+mon_cell

def getEvolutionTable(species):
    stages = getEvolutionData(species)
    if stages == -1:
        return -1
    row_strings= formatEvolutionRows(stages)
    table_text = '\n'.join(row_strings)
    return f"<table>\n{table_text}\n</table>\n"

def getSpeciesTypeStringHTML(typeList):
    # return '<br>'.join(['<img src=\"../../img/type/{type}.png\">'.format(type = s.lower()) for s in typeList])
    return '<br>'.join(['<img src=\"../../img/type/{type}.png\">'.format(type = s.lower()) for s in typeList])

def getDefenseRow(v):
    max_per_row = 16
    all_elem = ['<img src=\"../../img/type/{type}.png\" width=\"48\">'.format(type=tt.lower()) for tt in v]
    split_elem = [''.join(all_elem[n:n+max_per_row]) for n in range(0,len(all_elem), max_per_row)]
    return '<br>'.join(split_elem)


def getCompositeSpriteTable(name, type, ability, defense):
    species, form = getSpecies(name)
    imString = getPokemonImageHTML(species,form)
    formHeader = getSubsectionHeader(name)\
        .replace('#','')\
        .replace('\n', '').strip()
    header_text = ['', 'Type']
    col_span = [1, 1]
    if form != 'base':
        header_text[0] = formHeader
    if len(ability) > 0:
        header_text.append('Ability')
        col_span.append(1)
        prefix = ['(1) ', '(2) ', '(HA) ']
        abi_strings = [prefix[i]+ability[i] for i in range(0, len(ability))]
        join_abi_string = ' <br> '.join(abi_strings)
    if len(defense) > 0:
        def_content = ["<tr><td align=\"right\">{t}:</td><td colspan=\"{cs}\">{c}</td></tr>".format(t=k.strip(), c = getDefenseRow(v), cs = sum(col_span)-1)
             for k,v in defense.items()]
    body_head = '<table cellspacing=\"0\" cellpadding=\"0\"><tr>' +\
        ''.join(['<th colspan=\"{cs}\" align=\"center\">{h}</th>'.format(h = h, cs = col_span[i]) for i,h in enumerate(header_text)]) + '</tr>'
    body_foot = '</table>'
    im_col = '<td align="center";rowspan=\"{rs}\">{im}</td>'.format(rs = 1, im = imString)
    type_col = '<td align="center";rowspan=\"{rs}\">{c}</td>'.format(rs = 1, c = getSpeciesTypeStringHTML(type))

    cell_content = [im_col, type_col]
    if len(ability)>0:
        abi_col = '<td rowspan=\"{rs}\">{c}</td>'.format(rs = 1, c = join_abi_string)
        cell_content.append(abi_col)
    body_content = '<tr>{c}</tr>'.format(c=''.join(cell_content))
    if len(defense) > 0:
        body_content += '<tr><th colspan=\"{cs}\" align=\"center\">Defenses</th></tr>'.format(cs = sum(col_span))
        body_content += ''.join(def_content)
    return body_head+body_content+body_foot

def inline_remove(o_set, c):
    o_set.remove(c)
    return o_set

def getAllFormsSpriteTable(data):
    sprite_tables = []
    tab_name = []
    for d in data:
        formKeys = [f for f in d.keys() if isValid(d[f])]
        abi = []
        defs = []
        if 'Ability' in formKeys:
            abi = d['Ability']
        if 'Defenses' in formKeys:
            defs = d['Defenses']
        _table = getCompositeSpriteTable(d['Name'], type = d['TYPE'], ability=abi, defense=defs)
        tab_name.append(getSubsectionHeader(d['Name']).replace('#','').replace('\n', '').strip())
        sprite_tables.append(_table)
    if len(sprite_tables) == 1:
        return sprite_tables[0]
    tabbed_content = ['=== \"{h}\"\n\t{c}\n'.format(h=tab_name[i], c = st) for i,st in enumerate(sprite_tables)]
    return '\n'.join(tabbed_content)+'\n&nbsp;\n'

def getSubsetFields(l, fields):
    return [{k:p[k] for k in p.keys() if k in fields and isValid(p[k])} for p in l]

def removeEmptyFields(l):
    return [p for p in l if len(inline_remove(set(p.keys()), 'Name'))>0]

def getAllFormsEvolutionTable(data):
    _evol_string = [getEvolutionTable(d['Name'].lower()) for d in data]
    _evol_string = [s for s in _evol_string if s != -1]
    if len(_evol_string) > 1:
        raise RuntimeError
    if len(_evol_string) == 0:
        return -1
    return _evol_string[0]

def groupListByFields(data, fk):
    grouped_data = []
    for d in data:
        if len(grouped_data) == 0:
            d['Name'] = [d['Name']]
            grouped_data.append(d)
            continue
        _comp_dict = {k:d[k] for k in d.keys() if k in fk}
        _group_comp = [{k:p[k] for k in p.keys() if k in fk} for p in grouped_data]
        match_ind = _group_comp.index(_comp_dict) if _comp_dict in _group_comp else -1
        if match_ind == -1:
            d['Name'] = [d['Name']]
            grouped_data.append(d)
        else:
            grouped_data[match_ind]['Name'].append(d['Name'])   
    return grouped_data

def getAllFormsStatTable(data):
    _reduced_data = removeEmptyFields(data)
    if len(_reduced_data) == 1:
        _reduced_data[0]['Name']  = [_reduced_data[0]['Name'] ]
        return getStatTable_JointColumns(_reduced_data)
        # return getStatTable(_reduced_data)
    fk = ['STATS', 'VANILLA STATS']
    for i,d in enumerate(data):
        if i == 0:
            continue
        for k in fk:
            if k not in d.keys():
                data[i][k] = data[0][k]
    grouped_data = groupListByFields(data,fk)
    return getStatTable_JointColumns(grouped_data)
    
def getItemTableString(data):
    headers = [getSubsectionHeader(d['Name']).replace('#','') for d in data]
    content = [getItemString(d['Items']).replace('\n', '<br>') for d in data]

    html_header = '<tr>'+''.join([f'<th>{h}</th>' for h in headers])+'</tr>'
    html_content = '<tr>'+''.join([f'<td>{c}</td>' for c in content])+'</tr>'
    return '<table>{c}</table>\n'.format(c = html_header+'\n'+html_content+'\n')

def getAllFormsItemString(data):
    _reduced_data = removeEmptyFields(data)
    if len(_reduced_data) == 0:
        return -1
    if len(_reduced_data) == 1:
        return getItemString(_reduced_data[0]['Items'])
    return getItemTableString(_reduced_data)

def getAllFormsLevelUpTable(data):
    _reduced_data = removeEmptyFields(data)
    if len(_reduced_data) == 0:
        return -1
    if len(_reduced_data) == 1:
        return getLevelUpTableWithForms(_reduced_data)
    for i in range(1, len(data)):
        if 'Level Up Moves' not in data[i].keys():
            data[i]['Level Up Moves'] = data[0]['Level Up Moves']
    grouped_data = groupListByFields(data, ['Level Up Moves'])
    return getLevelUpTableWithForms(grouped_data)
    
def sanitizeTM_Dicts(data):
    out_data = data
    for i,d in enumerate(out_data):
        if 'TM Moves' in d.keys():
            for j,m in enumerate(d['TM Moves']):
                out_data[i]['TM Moves'][j]['Move Name'] = m['Name']
    return out_data

def getAllFormsTMTable(data):
    sani_data = sanitizeTM_Dicts(data)
    _reduced_data = removeEmptyFields(sani_data)
    if len(_reduced_data) == 0:
        return -1
    if len(_reduced_data) == 1:
        return getTMTableWithForms(_reduced_data)
    for i in range(1, len(sani_data)):
        if 'TM Moves' not in sani_data[i].keys():
            sani_data[i]['TM Moves'] = sani_data[0]['TM Moves']
    grouped_data = groupListByFields(sani_data, ['TM Moves'])
    return getTMTableWithForms(grouped_data)

def getAllFormsTutorTable(data):
    _reduced_data = removeEmptyFields(data)
    if len(_reduced_data) == 0:
        return -1
    if len(_reduced_data) == 1:
        return getTutorTableWithForms(_reduced_data)
    for i,d in enumerate(data):
        if 'Tutor Moves' not in d.keys():
            data[i]['Tutor Moves'] = data[0]['Tutor Moves']
    return getTutorTableWithForms(data)    
    
def makePageText(pokemonInformation):
    pageSections = []
    bodyIncludes = []

    if len(pokemonInformation) == 0:
        raise TypeError
    
    sprite_table_fields = ["Name", "TYPE", "Ability", "Defenses"]
    sprite_table_data = getSubsetFields(pokemonInformation, sprite_table_fields)
    sprite_table_string = getAllFormsSpriteTable(sprite_table_data)
    pageSections.append(sprite_table_string+'\n')

    evolution_table_fields = ["Name"]
    evolution_table_data = getSubsetFields(pokemonInformation, evolution_table_fields)
    evolution_table_string = getAllFormsEvolutionTable(evolution_table_data)
    if evolution_table_string != -1:
        pageSections.append('## Evolutions\n'+evolution_table_string+'\n')

    stat_table_fields = ["Name", "STATS", "VANILLA STATS"]
    stat_table_data = getSubsetFields(pokemonInformation, stat_table_fields)
    stat_table_string = getAllFormsStatTable(stat_table_data)
    pageSections.append('## Stats\n'+stat_table_string+'\n')

    item_table_fields = ["Name", "Items"]
    item_table_data = getSubsetFields(pokemonInformation, item_table_fields)
    item_table_string = getAllFormsItemString(item_table_data)
    if item_table_string != -1:
        pageSections.append('## Wild Hold Items\n'  + item_table_string +'\n')

    level_up_table_fields = ["Name", "Level Up Moves"]
    level_up_table_data = getSubsetFields(pokemonInformation,level_up_table_fields)
    level_up_table_string = getAllFormsLevelUpTable(copy.deepcopy(level_up_table_data))
    if level_up_table_data != -1:
        pageSections.append('## Level Up Moves\n' + level_up_table_string + '\n')

    tm_table_fields = ["Name", "TM Moves"]
    tm_table_data = getSubsetFields(pokemonInformation,tm_table_fields)
    tm_table_string = getAllFormsTMTable(copy.deepcopy(tm_table_data))
    if tm_table_string != -1:
        pageSections.append('## TM Moves\n' + tm_table_string + '\n')

    tutor_table_fields = ["Name", "Tutor Moves"]
    tutor_table_data = getSubsetFields(pokemonInformation, tutor_table_fields)
    tutor_table_string = getAllFormsTutorTable(tutor_table_data)
    if tutor_table_string != -1:
        pageSections.append('## Tutor Moves\n' + tutor_table_string + '\n')

    if 'Pre-Evolution Moves' in pokemonInformation[0].keys():
        preEvoString = getPreEvoMoveSection(pokemonInformation[0]['Pre-Evolution Moves'])
        pageSections.append('## Pre-Evolution Moves\n'+preEvoString +'\n')

    bodyText = '\n'.join(pageSections)
    return bodyIncludes, bodyText

def getPokemonMarkdown(pkmnInformation):
    headerText = getTopLevelHeader(pkmnInformation=pkmnInformation[0])
    page_includes, page_text = makePageText(pkmnInformation)
    tmp_incl = '\n'.join(page_includes)
    body_includes = "\n".join(list(OrderedDict.fromkeys(tmp_incl.split("\n"))))
    markdownText = '#' + headerText + '\n' + page_text
    includeText = '--8<-- "includes/abilities.md"\n\n' + body_includes + '\n'
    encounterIncl, encounterTable = getEncounters(pkmnInformation[0]['Name'])
    if encounterTable != '':
        markdownText += '\n## Encounter Locations\n\n'
        markdownText += encounterTable +'\n'
        includeText+=encounterIncl + '\n'
    markdownText += includeText
    number = pkmnInformation[0]['Number']
    natDexNumber = f"{number:03}"
    outfilename = natDexNumber+'.md'
    linkText = '- {htext}: pokemons/{fname}\n'.format(htext=headerText, fname = outfilename)
    return linkText, outfilename, markdownText