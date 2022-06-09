#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [0] * len(matrix)
    for i in range(len(matrix)):
        new_matrix[i] = [0] * len(matrix[0])
    for k in range(len(new_matrix)):
        for el in range(len(new_matrix[k])):
            new_matrix[k][el] = matrix[k][el]**2
    return new_matrix
