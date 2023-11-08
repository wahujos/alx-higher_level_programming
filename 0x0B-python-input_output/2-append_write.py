#!/usr/bin/python3
"""defining the module"""


def append_write(filename="", text=""):
    """defining the function"""
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
