#!/usr/bin/python3
for outer in range(10):
    for inner in range(10):
        if inner < outer or inner == outer:
            continue
        else:
            if outer == 8 and inner == 9:
                print("{}{}".format(outer, inner))
            else:
                print("{}{}".format(outer, inner), end=', ')
