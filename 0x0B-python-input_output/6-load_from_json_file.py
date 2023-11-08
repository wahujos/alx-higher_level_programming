#!/usr/bin/python3
"""defining the module"""
import json
"""handle json"""


def load_from_json_file(filename):
    """defining the function"""
    with open(filename) as f:
        data = f.read()
        return json.loads(data)
