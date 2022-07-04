if __name__ == "__main__":
    n = int(input())
    total_credits = 0
    total_GP = 0
    for i in range(n):
        info = input().split()
        mark = int(info[0])
        credit = float(info[1])
        if credit < 1:
            continue
        else:
            if mark >= 60:
                total_GP += credit * (4 - 3 * (100 - mark) * (100 - mark) / 1600)
            total_credits += credit
    print("%.2f" % float(total_GP / total_credits), end="")
