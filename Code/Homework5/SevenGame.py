if __name__ == "__main__":
    m, n, t = map(int, input().split())
    mark = [0 for i in range(m)]
    cnt = 1
    turns = 0
    while True:
        if turns == t:
            break
        for i in range(m):
            if (cnt % n == 0) | (str(cnt).find(str(n)) >= 0):
                mark[i] = 1
            cnt += 1
        turns += 1
    if min(mark) == 0:
        for i in range(len(mark)):
            if mark[i] == 0:
                print(i + 1, end=" ")
    else:
        print("NO")
