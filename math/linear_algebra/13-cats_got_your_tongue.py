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
