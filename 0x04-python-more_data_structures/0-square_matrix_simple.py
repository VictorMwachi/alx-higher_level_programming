#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        s_row = []
        for i in row:
            s_row.append(i**2)
        new_matrix.append(s_row)
    return new_matrix
