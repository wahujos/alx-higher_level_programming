#!/usr/bin/python3
for number in range(100):
    formatted = "{:02d}".format(number)
    print("{}, ".format(formatted), end='')
