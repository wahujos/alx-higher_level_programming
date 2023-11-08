#!/usr/bin/python3
"""Defining the modules"""
import json
"""handle json"""


def save_to_json_file(my_obj, filename):
    """defining the function"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
