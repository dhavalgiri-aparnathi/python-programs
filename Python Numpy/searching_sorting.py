import numpy as np

# searching

arr = np.array([20, 10, -30, 40])

print(np.where(arr == 20))

# searching sorted array

arr2 = np.array([10, 20, 30, 40, 50])

print(np.searchsorted(arr2, 40))

# sorting

arr3 = np.array([40, 50, -34, 0, 23, 45])

print(np.sort(arr3))

