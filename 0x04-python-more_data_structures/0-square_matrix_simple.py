#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [0] * len(matrix)
    for i in range(len(matrix)):
        new_matrix[i] = [0] * len(matrix)
    for k in range (len(new_matrix)):
        for l in range(len(new_matrix[k])):
            new_matrix[k][l] = matrix[k][l]**2
    return new_matrix
