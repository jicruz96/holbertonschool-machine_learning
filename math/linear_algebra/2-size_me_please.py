#!/usr/bin/env python3
"""
Module for exercise number 2 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""


def matrix_shape(matrix):
    """Compute the shape of a matrix.

    * You can assume all elements in the same dimension are of the same type
        and shape

    Returns:
        Shape of each dimension as a list of integers.
    """
    dimensions = []
    dimension = len(matrix)
    dimensions.append(dimension)
    if dimension > 0 and isinstance(matrix[0], list):
        next_dimensions = matrix_shape(matrix[0])
        dimensions.extend(next_dimensions)
    return dimensions


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    print(matrix_shape(mat1))
    mat2 = [
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]],
    ]
    print(matrix_shape(mat2))
