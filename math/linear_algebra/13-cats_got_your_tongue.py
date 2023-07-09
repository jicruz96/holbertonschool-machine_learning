#!/usr/bin/env python3
"""
Module for exercise number 13 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis
    """
    return np.concatenate((mat1, mat2), axis=axis)


if __name__ == "__main__":
    np_cat = __import__("13-cats_got_your_tongue").np_cat

    mat1 = np.array([[11, 22, 33], [44, 55, 66]])
    mat2 = np.array([[1, 2, 3], [4, 5, 6]])
    mat3 = np.array([[7], [8]])
    print(np_cat(mat1, mat2))
    print(np_cat(mat1, mat2, axis=1))
    print(np_cat(mat1, mat3, axis=1))
