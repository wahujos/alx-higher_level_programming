#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for v in a_dictionary:
            if v == key:
                a_dictionary[v] = value
    return a_dictionary
