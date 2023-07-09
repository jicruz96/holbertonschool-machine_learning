#!/usr/bin/env python3
"""
Module for exercise number 8 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""
from typing import List, Union

TwoDMatrixType = List[List[int]]


def mat_mul(
    mat1: TwoDMatrixType, mat2: TwoDMatrixType
) -> Union[TwoDMatrixType, None]:
    """performs a matrix multiplication between two 2D matrices.

    If the two matrices cannot be multiplied, returns None.
    """
    if len(mat1[0]) != len(mat2):
        return None
    mat2_cols = matrix_transpose(mat2)
    return [[dot_product(row, col) for col in mat2_cols] for row in mat1]


def matrix_transpose(matrix: TwoDMatrixType) -> TwoDMatrixType:
    """Returns the transposition of a non-empty 2D matrix."""
    return [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]


def dot_product(arr1: List[int], arr2: List[int]) -> int:
    """Computes the dot product of two arrays."""
    if len(arr1) != len(arr2):
        raise ValueError(
            "Cannot take the dot product of two vectors of different length"
        )
    return sum(arr1[i] * arr2[i] for i in range(len(arr1)))


if __name__ == "__main__":
    mat1 = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]
    mat2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]
    print(mat_mul(mat1, mat2))
