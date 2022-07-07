if __name__ == "__main__":
    n, k = map(int, input().split())
    type_1 = 0
    type_2 = 0
    sum_1 = 0
    sum_2 = 0
    for i in range(1, n + 1):
        if i % k == 0:
            sum_1 += i
            type_1 += 1
        else:
            sum_2 += i
            type_2 += 1
    print("%.1f %.1f" % (sum_1 / type_1, sum_2 / type_2))
