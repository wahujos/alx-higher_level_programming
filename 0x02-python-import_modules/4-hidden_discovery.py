#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names_defined = dir(hidden_4)
    for name in range(names_defined):
        if name[0] == '_':
            continue
        else:
            print({}.format(name))
