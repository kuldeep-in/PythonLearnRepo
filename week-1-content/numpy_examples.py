"""
A short demonstration of the Numpy library.
"""

import numpy as np

arr_1 = np.array([1, 3, 5])

print("Example Numpy array")
print(arr_1)

matrix_1 = [[1, 2],
           [3, 6]]

matrix_2 = [[4, 6],
            [5, 2]]

dot_prod = np.dot(matrix_1, matrix_2)

print("Dot product")
print(dot_prod)

arr_2 = np.array([1, 7])
arr_3 = np.array([3, 2])

cross_prod = np.cross(arr_2, arr_3)

print("Cross product")
print(cross_prod)
