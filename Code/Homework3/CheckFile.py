h = []
n, m = input().split(' ')
n = int(n)
m = int(m)


def inrange(i, j):
    global m, n
    if 0 <= i < n and 0 <= j < m:
        return True
    return False


def down(i, j):
    global h
    flag = 0
    s1 = 0
    if inrange(i - 1, j):
        if h[i - 1][j] < h[i][j]:
            s1 = down(i - 1, j) + 1
            flag = 1

    s2 = 0
    if inrange(i, j - 1):
        if h[i][j - 1] < h[i][j]:
            s2 = down(i, j - 1) + 1
            flag = 1

    s3 = 0
    if inrange(i + 1, j):
        if h[i + 1][j] < h[i][j]:
            s3 = down(i + 1, j) + 1
            flag = 1

    s4 = 0
    if inrange(i, j + 1):
        if h[i][j + 1] < h[i][j]:
            s4 = down(i, j + 1) + 1
            flag = 1
    if flag == 0:
        return 1
    return max(s1, s2, s3, s4)


for i in range(n):
    s = input().split(' ')
    l = []
    for j in s:
        l.append(int(j))
    h.append(l)

maxlen = 0
for i in range(n):
    for j in range(m):
        a = down(i, j)
        if a > maxlen:
            maxlen = a
print(maxlen)
