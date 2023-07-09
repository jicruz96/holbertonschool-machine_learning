#!/usr/bin/env python3
"""
Module for exercise number 3 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""


def matrix_transpose(matrix):
    """Returns the transposition of a non-empty 2D matrix."""
    return [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    print(mat1)
    print(matrix_transpose(mat1))
    mat2 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
        [26, 27, 28, 29, 30],
    ]
    print(mat2)
    print(matrix_transpose(mat2))
