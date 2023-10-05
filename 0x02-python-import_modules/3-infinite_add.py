#!/usr/bin/python3
import sys


def calculate_sum():
    total = 0
    num_args = len(sys.argv) - 1
    for num in range(num_args):
        total += int(sys.argv[num + 1])
    return total


if __name__ == "__main__":
    result = calculate_sum()
    print(result)
