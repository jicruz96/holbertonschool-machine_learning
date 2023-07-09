#!/usr/bin/env python3
"""
Module for exercise number 102 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices of any dimension along a specific axis
    """
    mat1_shape = matrix_shape(mat1)
    mat2_shape = matrix_shape(mat2)
    # matricies must have the same number of dimensions
    if len(mat1_shape) != len(mat2_shape):
        return None
    # all dimensions except the axis must be the same
    for i in range(len(mat1_shape)):
        if i != axis and mat1_shape[i] != mat2_shape[i]:
            return None

    return _cat_matrices_helper(mat1, mat2, axis)


def _cat_matrices_helper(mat1, mat2, axis):
    """
    Helper function for cat_matrices
    """
    if axis == 0:
        return mat1 + mat2
    return [
        _cat_matrices_helper(mat1[i], mat2[i], axis - 1)
        for i in range(len(mat1))
    ]


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


# import time

# import numpy as np


# def _run_cat_matrices_and_compare_to_np(mat1, mat2, axis=0):
#     """
#     Runs the cat_matrices function and compares the result to the
#     numpy concatenate function
#     """
#     print("-------------------")
#     t = time.time()
#     print(cat_matrices(mat1, mat2, axis=axis))
#     print("Python:", time.time() - t)
#     t = time.time()
#     np.concatenate((np.array(mat1), np.array(mat2)), axis=axis)
#     print("NumPy:", time.time() - t)
#     print("-------------------\n\n")


# _run_cat_matrices_and_compare_to_np([1, 2, 3], [4, 5, 6])
# mat1 = [[1, 2], [3, 4]]
# mat2 = [[5, 6], [7, 8]]
# mat3 = [
#     [
#         [[1, 2, 3, 4], [5, 6, 7, 8]],
#         [[9, 10, 11, 12], [13, 14, 15, 16]],
#         [[17, 18, 19, 20], [21, 22, 23, 24]],
#     ],
#     [
#         [[25, 26, 27, 28], [29, 30, 31, 32]],
#         [[33, 34, 35, 36], [37, 38, 39, 40]],
#         [[41, 42, 43, 44], [45, 46, 47, 48]],
#     ],
# ]
# mat4 = [
#     [
#         [[11, 12, 13, 14], [15, 16, 17, 18]],
#         [[19, 110, 111, 112], [113, 114, 115, 116]],
#         [[117, 118, 119, 120], [121, 122, 123, 124]],
#     ],
#     [
#         [[125, 126, 127, 128], [129, 130, 131, 132]],
#         [[133, 134, 135, 136], [137, 138, 139, 140]],
#         [[141, 142, 143, 144], [145, 146, 147, 148]],
#     ],
# ]
# mat5 = [
#     [
#         [[11, 12, 13, 14], [15, 16, 17, 18]],
#         [[117, 118, 119, 120], [121, 122, 123, 124]],
#     ],
#     [
#         [[125, 126, 127, 128], [129, 130, 131, 132]],
#         [[141, 142, 143, 144], [145, 146, 147, 148]],
#     ],
# ]
# _run_cat_matrices_and_compare_to_np(mat1, mat2)
# _run_cat_matrices_and_compare_to_np(mat1, mat2, axis=1)
# _run_cat_matrices_and_compare_to_np(mat3, mat4, axis=3)
# _run_cat_matrices_and_compare_to_np(mat3, mat5, axis=1)

# # this one should print `None` because the matrices cannot be concatenated
# print(cat_matrices(mat2, mat5))
