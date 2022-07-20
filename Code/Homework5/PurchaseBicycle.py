if __name__ == "__main__":
    n = int(input())
    bicycle_price = list(map(int, input().split()))
    sale_price = list(map(int, input().split()))
    fix_price = list(map(int, input().split()))
    price_list = [[0 for i in range(n)] for j in range(n)]
    price_list[0][0] = bicycle_price[0] + fix_price[0]
    for i in range(1, n):
        temp = []
        for j in range(0, i):
            temp.append(price_list[i - 1][j] + bicycle_price[i] - sale_price[j] + fix_price[0])
        price_list[i][0] = min(temp)
        for j in range(1, i + 1):
            price_list[i][j] = price_list[i - 1][j - 1] + fix_price[j]
    result = []
    for i in range(n):
        result.append(price_list[n - 1][i] - sale_price[i])
    print(min(result))
