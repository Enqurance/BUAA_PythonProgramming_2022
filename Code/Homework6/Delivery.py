import math

distances = []


def search(dis, v, arr, index):
    global distances
    if min(v) == 1:
        dis += cal_len(arr[0][0], arr[0][1], arr[index][0], arr[index][1])
        distances.append(dis)
        return
    for i in range(len(arr)):
        if v[i] == 0:
            v[i] = 1
            search(dis + cal_len(arr[i][0], arr[i][1], arr[index][0], arr[index][1]), v, arr, i)
            v[i] = 0


def cal_len(x1, y1, x2, y2):
    return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))


if __name__ == "__main__":
    n = int(input())
    mark = [[0, 0] for i in range(n + 1)]
    visited = [0 for i in range(n + 1)]
    visited[0] = 1
    for i in range(n + 1):
        mark[i][0], mark[i][1] = map(int, input().split())
    search(0, visited, mark, 0)
    print("%.2f" % min(distances))
