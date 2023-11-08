#!/usr/bin/python3
"""defining te module"""


def write_file(filename="", text=""):
    """defining the function"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
