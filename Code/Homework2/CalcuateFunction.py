import math


def f(x):
    if x == 0:
        return 1
    elif x == 1:
        return 3
    else:
        return (f(x - 2) + f(x - 1)) / (math.pow(1.01, f(x - 1)))


if __name__ == "__main__":
    n = int(input())
    print("%.2f" % f(n))
