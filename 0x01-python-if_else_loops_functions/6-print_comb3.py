#!/usr/bin/python3
for first in range(10):
    for second in range(first + 1, 10):
        print("{:02d}, ".format(first * 10 + second), end='')
print()
