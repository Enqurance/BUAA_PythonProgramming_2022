length = []


def get_matrix(n, array):
    for i in range(n):
        temp = list(map(int, input().split()))
        array.append(temp)


def get_max(n, m, array):
    max_height = -1
    for i in range(n):
        for j in range(m):
            if int(array[i][j]) > max_height:
                max_height = int(array[i][j])
    return int(max_height)


def in_range(x_max, x_pos, y_max, y_pos):
    return 0 <= x_pos < x_max and 0 <= y_pos < y_max


def deep_search(x_max, x_pos, y_max, y_pos, array, dis):
    if in_range(x_max, x_pos, y_max, y_pos):
        length.append(dis)
        if in_range(x_max, x_pos - 1, y_max, y_pos) and array[x_pos][y_pos] > array[x_pos - 1][y_pos]:
            deep_search(x_max, x_pos - 1, y_max, y_pos, array, dis + 1)
        if in_range(x_max, x_pos + 1, y_max, y_pos) and array[x_pos][y_pos] > array[x_pos + 1][y_pos]:
            deep_search(x_max, x_pos + 1, y_max, y_pos, array, dis + 1)
        if in_range(x_max, x_pos, y_max, y_pos - 1) and array[x_pos][y_pos] > array[x_pos][y_pos - 1]:
            deep_search(x_max, x_pos, y_max, y_pos - 1, array, dis + 1)
        if in_range(x_max, x_pos, y_max, y_pos + 1) and array[x_pos][y_pos] > array[x_pos][y_pos + 1]:
            deep_search(x_max, x_pos, y_max, y_pos + 1, array, dis + 1)


if __name__ == "__main__":
    x, y = map(int, input().split())
    arr = []
    get_matrix(x, arr)
    max_h = get_max(x, y, arr)
    for i1 in range(x):
        for j1 in range(y):
            if arr[i1][j1] == max_h:
                deep_search(x, i1, y, j1, arr, 1)
    print(max(length))
    # print(arr)
