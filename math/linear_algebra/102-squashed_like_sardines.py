#!/usr/bin/env python3
"""
Module for exercise number 102 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices of any dimension along a specific axis
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [i.copy() for i in mat1] + [i.copy() for i in mat2]
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i].copy() + mat2[i].copy() for i in range(len(mat1))]
    if axis == 2:
        if len(mat1) != len(mat2):
            return None
        return [cat_matrices(mat1[i], mat2[i]) for i in range(len(mat1))]
    return None
