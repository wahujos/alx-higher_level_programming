#!/usr/bin/python3
"""defination of the modules"""
import sys
 
from '5-save_to_json_file' import save_to_json_file
from '6-load_from_json_file' import load_from_json_file

args = sys.argv[1:]
load_list = []
with open('add_item.json') as file:
    load_from_json_file('add_item.json')

load_list.extend(args)
save_to_json_file(load_list, 'add_item.json')

