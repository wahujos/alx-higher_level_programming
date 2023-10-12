#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_dict = a_dictionary.copy()
    for k, v in copy_dict.items():
        if v == value:
            del a_dictionary[k]
        else:
            continue
    return a_dictionary
