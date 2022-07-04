if __name__ == "__main__":
    n = int(input())
    if n % 2 == 0:
        for i in range(n):
            for j in range(n - i - 1):
                print(" ", end="")
            for j in range(i + 1):
                print("\"", end="")
            if i != n - 1:
                print()
    else:
        for i in range(n):
            for j in range(n - i - 1):
                print(" ", end="")
            for j in range(i + 1):
                print("\\", end="")
            if i != n - 1:
                print()
