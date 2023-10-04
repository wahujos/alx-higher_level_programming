#!/usr/bin/python3
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter == 'q' or letter == 'e':
        continue
    print("{}".format(letter), end='')
