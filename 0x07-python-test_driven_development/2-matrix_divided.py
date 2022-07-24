#!/usr/bin/python3
def matrix_divided(matrix, div):
    """divides evey element in a matrix"""
    new_matrix = []
    for row in matrix:
        for i in row:
            if type(i) != float or type(i) != int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int or type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(i/div)
        new_matrix.append(new_row)
    return new_matrix    
