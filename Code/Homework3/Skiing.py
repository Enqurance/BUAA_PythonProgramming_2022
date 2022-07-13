import numpy as np

length = []


def get_matrix(n, m, array):
    max_height = -1
    for i in range(n):
        ele = input().split()
        for j in range(m):
            array[i][j] = int(ele[j])
            if int(ele[j]) > max_height:
                max_height = int(ele[j])
    return max_height


def get_min(n, m, array):
    min_height = 1000000001
    for i in range(n):
        for j in range(m):
            if array[i][j] < min_height:
                min_height = array[i][j]
    return int(min_height)


def in_range(x_max, x_pos, y_max, y_pos):
    return 0 <= x_pos < x_max and 0 <= y_pos < y_max


def deep_search(x_max, x_pos, y_max, y_pos, array, dis, min_num):
    if in_range(x_max, x_pos, y_max, y_pos):
        length.append(dis)
        if in_range(x_max, x_pos - 1, y_max, y_pos) and array[x_pos][y_pos] > array[x_pos - 1][y_pos]:
            deep_search(x_max, x_pos - 1, y_max, y_pos, array, dis + 1, min_num)
        if in_range(x_max, x_pos + 1, y_max, y_pos) and array[x_pos][y_pos] > array[x_pos + 1][y_pos]:
            deep_search(x_max, x_pos + 1, y_max, y_pos, array, dis + 1, min_num)
        if in_range(x_max, x_pos, y_max, y_pos - 1) and array[x_pos][y_pos] > array[x_pos][y_pos - 1]:
            deep_search(x_max, x_pos, y_max, y_pos - 1, array, dis + 1, min_num)
        if in_range(x_max, x_pos, y_max, y_pos + 1) and array[x_pos][y_pos] > array[x_pos][y_pos + 1]:
            deep_search(x_max, x_pos, y_max, y_pos + 1, array, dis + 1, min_num)


if __name__ == "__main__":
    x, y = map(int, input().split())
    arr = np.zeros((x, y))
    max_h = get_matrix(x, y, arr)
    min_h = get_min(x, y, arr)
    for i1 in range(x):
        for j1 in range(y):
            deep_search(x, i1, y, j1, arr, 1, min_h)
    print(max(length))
    # print(arr)
    # print(max_h)
    # print(min_h)
    # print(length)
