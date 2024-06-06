from genericpath import isfile
import os
import tqdm
import json
import csv
import re

mart_item_file = './ItemChanges/MartsList.txt'
mart_outfile = 'includes/mart_items.md'
with open(mart_item_file, mode = 'r') as mart_file:
    doc_lines = mart_file.read().splitlines()

mart_tables = []
tmp_table = ''
for line in doc_lines:
    # Start a new table
    if len(line) == 0:
        tmp_table += "</table>\n"
        mart_tables.append(tmp_table)
        tmp_table = ""
        continue
    if '\t' not in line:
        tmp_table = "<table>\n<tr><th colspan=\"2\">{text}</th></tr>\n".format(text=line.strip())
    else:
        mart_entry = line.split('\t')
        tmp_table += "<tr><td style=\"vertical-align: middle; word-wrap: break-word; text-align: center;\">{mart}</td><td>{items}</td></tr>\n".format(mart=mart_entry[0], items=mart_entry[1])
    
with open(mart_outfile, mode = 'w') as out:
    out.write('\n\n'.join(mart_tables))