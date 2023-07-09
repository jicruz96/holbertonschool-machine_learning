#!/usr/bin/env python3

import time

import numpy as np


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list of lists): first given matrix
        mat2 (list of lists): second given matrix
        axis (int): axis to concatenate along

    Returns:
        list of lists: concatenated matrix
    """
    try:
        return np.concatenate((np.array(mat1), np.array(mat2)), axis=axis)
    except ValueError:
        return None
