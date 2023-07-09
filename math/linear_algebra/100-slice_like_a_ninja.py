#!/usr/bin/env python3

import numpy as np


def np_slice(matrix, axes={}):
    """
    Slices a matrix along specific axes.

    Args:
        matrix (numpy.ndarray): matrix to slice
        axes (dict): dictionary where the key is an axis to slice along and
            the value is a tuple representing the slice to make along that axis
    """
    DEFAULT_SLICE = slice(None, None, None)  # slice to select everything
    slices = [slice(*axes.get(i, DEFAULT_SLICE)) for i in range(matrix.ndim)]
    return matrix[tuple(slices)]


if __name__ == "__main__":
    mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(np_slice(mat1, axes={1: (1, 3)}))
    print(mat1)
    mat2 = np.array(
        [
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
            [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
            [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]],
        ]
    )
    print(np_slice(mat2, axes={0: (2,), 2: (None, None, -2)}))
    print(mat2)
