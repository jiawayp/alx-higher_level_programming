#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    return [[new_matrix**2 for new_matrix in row] for row in matrix]
