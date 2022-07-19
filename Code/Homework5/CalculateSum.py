if __name__ == "__main__":
    l = int(input())
    x_nums = list(map(int, input().split()))
    y_nums = list(map(int, input().split()))
    x_s = [x_nums[0]]
    for i in range(1, l):
        x_s.append(x_s[i - 1] + x_nums[i])
    ans = 0
    for i in range(l):
        ans += y_nums[i] * x_s[i]
    print(ans)
