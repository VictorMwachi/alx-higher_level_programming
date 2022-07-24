#!/usr/bin/python3
def matrix_divided(matrix, div):
    """divides evey element in a matrix"""
    for row in matrix:
        for i in row:
            if type(i) != float or type(i) != int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

