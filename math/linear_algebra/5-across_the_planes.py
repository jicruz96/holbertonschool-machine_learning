#!/usr/bin/env python3
"""
Module for exercise number 5 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""


def add_matrices2D(mat1, mat2):
    """adds two 2D matrices element-wise.

    If matrices are not the same shape, returns None.
    """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    return [add_arrays(mat1[i], mat2[i]) for i in range(len(mat1))]


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


def add_arrays(arr1, arr2):
    """
    adds two same-length lists element-wise.

    If lists are not the same length, returns None.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, mat2))
    print(mat1)
    print(mat2)
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
