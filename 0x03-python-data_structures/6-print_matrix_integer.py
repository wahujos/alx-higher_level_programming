#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for num in row:
            if row.index(num) == (len(row) - 1):
                print("{}".format(num), end='')
                continue
            print("{}".format(num), end=' ')
        print()
