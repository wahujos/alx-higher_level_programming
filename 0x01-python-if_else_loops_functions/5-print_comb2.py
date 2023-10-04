#!/usr/bin/python3
for number in range(99):
    formatted = "{:02d}".format(number)
    print("{}, ".format(formatted), end='')
print('99')
