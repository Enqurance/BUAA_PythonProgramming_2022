import numpy as np

a = np.zeros((4, 4))

for i in range(4):
    nums = input().split()
    for j in range(4):
        a[i][j] = int(nums[j])
rank = int(np.linalg.det(a))
print(rank)
