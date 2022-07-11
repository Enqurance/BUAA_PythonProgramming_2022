import math


def get_lcm():
    l = []
    n = int(input())
    for i in range(n):
        l.append(int(input()))
    if n == 1:
        return l[0]
    temp = l[0]
    length = len(l)
    for i in range(1, length):
        temp = temp // math.gcd(temp, l[i]) * l[i]
    return temp


def get_nums():
    nums = []
    for i in range(1, 10):
        string = str(i)
        nums.append(string[0] + string[0])
    for i in range(10, 100):
        string = str(i)
        nums.append(string[0:2] + string[0])
        nums.append(string[0:2] + string[-1:-3:-1])
    for i in range(100, 1000):
        string = str(i)
        nums.append(string[0:3] + string[-2:-4:-1])
        nums.append(string[0:3] + string[-1:-4:-1])
    for i in range(1000, 10000):
        string = str(i)
        nums.append(string[0:4] + string[-2:-5:-1])
        nums.append(string[0:4] + string[-1:-5:-1])
    return nums


if __name__ == "__main__":
    lcm = get_lcm()
    checks = get_nums()
    printed = False
    # print(len(checks))
    # print(lcm)
    output = []
    for i in checks:
        if int(i) % lcm == 0:
            output.append(int(i))
    if len(output) == 0:
        print(None)
    else:
        output.sort()
        for k in output:
            print(k)
