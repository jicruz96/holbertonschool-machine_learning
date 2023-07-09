#!/usr/bin/env python3
"""
Module for exercise number 12 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""

from typing import Tuple

import numpy as np


def np_elementwise(
    mat1, mat2
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    performs element-wise addition, subtraction, multiplication, and division.

    Returns:
        tuple containing the element-wise sum, difference, product, and
        quotient, respectively
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2


if __name__ == "__main__":
    mat1 = np.array([[11, 22, 33], [44, 55, 66]])
    mat2 = np.array([[1, 2, 3], [4, 5, 6]])

    print(mat1)
    print(mat2)
    add, sub, mul, div = np_elementwise(mat1, mat2)
    print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
    add, sub, mul, div = np_elementwise(mat1, 2)
    print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
