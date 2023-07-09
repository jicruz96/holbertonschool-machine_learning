#!/usr/bin/env python3
"""
Module for exercise number 100 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""


def np_slice(matrix, axes={}):
    """
    Slices a matrix along specific axes.

    Args:
        matrix (numpy.ndarray): matrix to slice
        axes (dict): dictionary where the key is an axis to slice along and
            the value is a tuple representing the slice to make along that axis
    """
    DEFAULT_SLICE = (None, None, None)  # slice to select everything
    slices = [slice(*axes.get(i, DEFAULT_SLICE)) for i in range(matrix.ndim)]
    return matrix[tuple(slices)]
