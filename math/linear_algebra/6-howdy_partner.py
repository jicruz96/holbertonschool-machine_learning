#!/usr/bin/env python3


def cat_arrays(arr1, arr2):
    """concatenates two lists"""
    return arr1 + arr2


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8]
    print(cat_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
