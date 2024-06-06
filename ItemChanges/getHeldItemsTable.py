from genericpath import isfile
import os
import tqdm
import json
import csv
import re

def get_link(num):
    return f"https://smilingzero.github.io/BlazeBlack2ReduxWiki/pokemons/{num:03}/"

def getint(name):
    basename = name.partition('.')
    return int(basename[0])


pkmnDir = 'scrapedJSON/pokemon/'
listOfPokemonFiles = os.listdir(pkmnDir)
listOfPokemonFiles.sort(key=getint)

#####
# Scrape JSON
#####
pkmn_item_list = []
for ind, jsonFile in enumerate(tqdm.tqdm(listOfPokemonFiles)):
    with open(pkmnDir+jsonFile) as pkmnFile:
        loaded_json_info = json.load(pkmnFile)
        for pkmnInformation in loaded_json_info:
            if "Items" not in pkmnInformation.keys() or len(pkmnInformation["Items"]) == 0:
                continue
            subset_information = {k:v for k,v in pkmnInformation.items() if k in {'Number', 'Name', 'Items'}}
            pkmn_item_list.append(subset_information)



#####
# Reorganize list into dict of item: urls
#####
item_pkmn_dict = {}
for ind,entry in enumerate(tqdm.tqdm(pkmn_item_list)):
    this_pkmn = entry['Name']
    this_number = entry['Number']
    this_items = set([v for k,v in entry['Items'].items()])

    this_link = "<a href=\"{url}\">{name}</a>".format(url = get_link(this_number), name=this_pkmn)

    for this_item in this_items:
        if this_item in item_pkmn_dict.keys():
            item_pkmn_dict[this_item].append(this_link)
        else:
            item_pkmn_dict[this_item] = [this_link]

sorted_item_names = sorted(item_pkmn_dict.keys(), key=str.lower)

#####
# Make HTML table...
#####

def pkmnCell(link):
    return f'<td style="vertical-align: middle;">{link}</td>'

def wrapRow(content):
    return f'<tr>\n{content}\n</tr>'

def getItemRow(item_name, link, nRow):
    first_col = f'<td rowspan="{nRow}" style="vertical-align: middle;">{item_name}</td>'
    second_col = pkmnCell(link)
    return wrapRow(first_col + '\n' + second_col)

table_string = ''
list_of_row_strings = [wrapRow('<th colspan="2">Wild Hold Items</th>')]
for item_name in sorted_item_names:
    links = sorted(item_pkmn_dict[item_name])
    nRows = len(links)
    this_item_string = getItemRow(item_name, links[0], nRows)
    if nRows > 1:
        other_links = '\n'.join([wrapRow(pkmnCell(link)) for link in links[1:]])
        this_item_string += '\n'+other_links
    list_of_row_strings.append(this_item_string)
table_string = '<table>\n' + '\n'.join(list_of_row_strings) + '\n</table>'

with open('./includes/tmpHeldItemTable.md','w') as outFile:
    outFile.write(table_string)