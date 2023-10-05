#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("{:d} arguments.".format(num_args))
    elif num_args == 1:
        print("{:d} argument:".format(num_args))
        for i in range(num_args):
            print("{:d}: {}".format(num_args, sys.argv[i + 1]))
    elif num_args > 1:
        print("{:d} arguments:".format(num_args))
        for i in range(num_args):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))

