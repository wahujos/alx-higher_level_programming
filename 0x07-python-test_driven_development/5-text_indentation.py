#!/usr/bin/python3
'''
text indentation
'''


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters_given = [".", "?", ":"]
    res = ""
    for char in text:
        res += char
        if char in characters_given:
            res += "\n\n"
    print(res)
