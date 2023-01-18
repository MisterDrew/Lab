import numpy as np

x_0 = y_0 = 1
r1 = 3
n_points = 20
time = 1
h = 0.01

a = np.array([
    [ 0, 0, 0, 0],
    [ 1 / 3, 0, 0, 0],
    [ 0, 2 / 3, 0, 0],
    [ 0, 0, 0, 0],
])

b = np.array([1 / 4, 0, 3 / 4, 0])
c = np.array([0, 1 / 3, 2 / 3, 0])
