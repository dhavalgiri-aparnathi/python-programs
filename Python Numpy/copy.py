import numpy as np

arr = np.array([10, 20, 30, 40, 50])

copied_arr = arr.copy()

copied_arr[0] = 12

print(arr)
print(copied_arr)
