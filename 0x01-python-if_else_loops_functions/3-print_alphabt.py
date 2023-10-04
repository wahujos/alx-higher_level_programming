#!/usr/bin/python3
for letter in 'abcdefghijklmnopqrstuvwzyz':
    if letter == 'q' or letter == 'e':
        continue
    print("{}".format(letter), end='')
