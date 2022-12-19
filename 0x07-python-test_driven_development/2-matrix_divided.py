#!/usr/bin/python3
"""Matrix division"""


def matrix_divided(matrix, div):
    new_mat = list(matrix)
    if new_mat is matrix:
        print("help")
    leng = len(new_mat)
    
    #if (all(isinstance(item, (int, float)) for item in matrix) is False):
        #raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(leng):
        if len(new_mat[0]) != len(new_mat[i]):
            raise TypeError("Each row of the matrix must have the same size")

    if isinstance(div, (int,float)) is False:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    rowLength = len(new_mat[0])
    
    for i in range (leng):
        for j in range(rowLength):
            temp = new_mat[i][j]
            if isinstance(temp, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_mat[i][j] = round(temp / div, 2)
    
    return (new_mat)
