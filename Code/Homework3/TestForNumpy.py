import numpy as np

x, y = input().split()
arr = np.zeros((int(x), int(y)))
print(arr)
arr[1][2] = 3
print(arr)
