def get_min(m, n):
    if m < n:
        return m
    else:
        return n


def get_max(m, n):
    if m > n:
        return m
    else:
        return n


def which_str(m, n):
    if m > n:
        return 1
    else:
        return 2


if __name__ == "__main__":
    x = int(input())
    num_1 = str(input())
    num_2 = str(input())
    num_1 = num_1[-1::-1]
    num_2 = num_2[-1::-1]
    len_1 = len(num_1)
    len_2 = len(num_2)
    len_min = get_min(len_1, len_2)
    len_max = get_max(len_1, len_2)
    ans = []
    filled = 0
    for i in range(len_min):
        res = int(num_1[i]) + int(num_2[i]) + filled
        ans.append(res % x)
        if res >= x:
            filled = 1
        else:
            filled = 0
    if which_str(len_1, len_2) == 1:
        for i in range(len_min, len_max):
            res = int(num_1[i]) + filled
            ans.append(res % x)
            if res >= x:
                filled = 1
            else:
                filled = 0
    else:
        for i in range(len_min, len_max):
            res = int(num_2[i]) + filled
            ans.append(res % x)
            if res >= x:
                filled = 1
            else:
                filled = 0
    if filled == 1:
        ans.append(1)
    ans = ans[-1::-1]
    for item in ans:
        print(item, end="")
