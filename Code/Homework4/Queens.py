import copy

temp = [0 for j in range(8)]


def queen(i, lists):
    if i == 8:
        lists.append(copy.deepcopy(temp))
        return
    for j in range(8):
        k = 0
        while k < i:
            if (temp[k] == j) | ((k - i) == (temp[k] - j)) | ((i - k) == (temp[k] - j)):
                break
            k += 1
        if k == i:
            temp[i] = j
            queen(i + 1, lists)


if __name__ == "__main__":
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    chessboard = []
    cnt = 0
    queen(0, chessboard)
    for item in chessboard:
        if item[x] == y:
            cnt += 1
    print(cnt)
