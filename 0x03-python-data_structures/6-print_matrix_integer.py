#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lis_t in matrix:
        for i in lis_t:
            print("{:d}".format(i), end=" " if i != lis_t[-1] else "")
        print()
