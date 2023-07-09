#!/usr/bin/env python3
"""
Module for exercise number 12 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""


def np_elementwise(mat1, mat2):
    """
    performs element-wise addition, subtraction, multiplication, and division.

    Returns:
        tuple containing the element-wise sum, difference, product, and
        quotient, respectively
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
