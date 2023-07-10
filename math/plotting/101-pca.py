#!/usr/bin/env python3
"""
Principle Component Analysis (PCA) is a vital procedure used in data science
for reducing the dimensionality of data (in turn, decreasing computation cost).
It is also largely used for visualizing high dimensional data in 2 or 3
dimensions. For this task, you will be visualizing the Iris flower data set.
"""
from enum import Enum

import matplotlib.pyplot as plt
import numpy as np

"""
Use the file pca.npz to test your code.

Details:

* The title of the plot should be PCA of Iris Dataset
* `data` is a np.ndarray of shape (150, 4)
    * 150 => the number of flowers
    * 4 => petal length, petal width, sepal length, sepal width
* `labels` is a np.ndarray of shape (150,) containing information about what
  species of iris each data point represents:
    * 0 => Iris Setosa
    * 1 => Iris Versicolor
    * 2 => Iris Virginica
* `pca_data` is a np.ndarray of shape (150, 3)
    * The columns of pca_data represent the 3 dimensions of the reduced data,
      i.e., x, y, and z, respectively
* The x, y, and z axes should be labeled U1, U2, and U3, respectively
* The data points should be colored based on their labels using the plasma
  color map

"""


class Flower(Enum):
    Iris_setosa = 0
    Iris_versicolor = 1
    Iris_virginica = 2


lib = np.load("pca.npz")
data = lib["data"]
assert isinstance(data, np.ndarray), "data should be numpy.ndarray"
assert data.shape == (150, 4), "data should have 150 rows and 4 columns"
labels = lib["labels"]
assert isinstance(labels, np.ndarray), "labels should be numpy.ndarray"
assert labels.shape == (150,), "labels should have 150 rows"


data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)
assert isinstance(pca_data, np.ndarray), "pca_data should be numpy.ndarray"
assert pca_data.shape == (150, 3), "pca_data should have 150 rows & 3 columns"

x_axis = pca_data[:, 0]
y_axis = pca_data[:, 1]
z_axis = pca_data[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x_axis, y_axis, z_axis, c=labels, cmap="plasma")
ax.set_xlabel("U1")
ax.set_ylabel("U2")
ax.set_zlabel("U3")
plt.title("PCA of Iris Dataset")
plt.show()
