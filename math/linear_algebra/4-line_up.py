#!/usr/bin/env python3
"""
Module for exercise number 4 for the numpy and linear algebra
project (https://intranet.hbtn.io/projects/2275)
"""


def add_arrays(arr1, arr2):
    """
    adds two same-length lists element-wise.

    If lists are not the same length, returns None.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print(add_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
    print(add_arrays(arr1, [1, 2, 3]))
