#!/usr/bin/env python3


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices along an axis

    if the two matrices cannot be concatenated, returns None.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [[col for col in row] for row in mat1 + mat2]
    if len(mat1) != len(mat2):
        return None
    cat = []
    for i in range(len(mat1)):
        new_row = cat_arrays(mat1[i], mat2[i])
        if new_row is None:
            return None
        cat.append(new_row)
    return cat


def cat_arrays(arr1, arr2):
    """concatenates two lists"""
    return arr1 + arr2


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6]]
    mat3 = [[7], [8]]
    mat4 = cat_matrices2D(mat1, mat2)
    mat5 = cat_matrices2D(mat1, mat3, axis=1)
    print(mat4)
    print(mat5)
    mat1[0] = [9, 10]
    mat1[1].append(5)
    print(mat1)
    print(mat4)
    print(mat5)
