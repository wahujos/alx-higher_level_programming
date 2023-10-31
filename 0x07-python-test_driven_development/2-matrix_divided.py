#!/usr/bin/python3
'''
a function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    new_matrix = []
    if not matrix:
        raise Exception
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        new_row = []
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError
            ("matrix must be a matrix (list of lists) of integers/floats")
            res = value / div
            new_row.append(round(res, 2))
        new_matrix.append(new_row)
    return new_matrix
