def print_gold(temp_list):
    total_list = []
    for k in temp_list.keys():
        temp = [k, temp_list.get(k)[0]]
        total_list.append(temp)
    length = len(total_list)
    i1 = 0
    while i1 < length - 1:
        i2 = 0
        while i2 < length - i1 - 1:
            if total_list[i2][1] < total_list[i2 + 1][1]:
                temp = total_list[i2]
                total_list[i2] = total_list[i2 + 1]
                total_list[i2 + 1] = temp
            elif total_list[i2][1] == total_list[i2 + 1][1]:
                if total_list[i2][0] > total_list[i2 + 1][0]:
                    temp = total_list[i2]
                    total_list[i2] = total_list[i2 + 1]
                    total_list[i2 + 1] = temp
            i2 += 1
        i1 += 1
    for k in total_list:
        print(k[0] +
              " " + str(temp_list.get(k[0])[0]) +
              " " + str(temp_list.get(k[0])[1]) +
              " " + str(temp_list.get(k[0])[2]))


def print_total(temp_list):
    total_list = []
    for k in temp_list.keys():
        temp = [k, temp_list.get(k)[0] + temp_list.get(k)[1] + temp_list.get(k)[2]]
        total_list.append(temp)
    length = len(total_list)
    i1 = 0
    while i1 < length - 1:
        i2 = 0
        while i2 < length - i1 - 1:
            if total_list[i2][1] < total_list[i2 + 1][1]:
                temp = total_list[i2]
                total_list[i2] = total_list[i2 + 1]
                total_list[i2 + 1] = temp
            elif total_list[i2][1] == total_list[i2 + 1][1]:
                if total_list[i2][0] > total_list[i2 + 1][0]:
                    temp = total_list[i2]
                    total_list[i2] = total_list[i2 + 1]
                    total_list[i2 + 1] = temp
            i2 += 1
        i1 += 1
    for k in total_list:
        print(k[0] +
              " " + str(temp_list.get(k[0])[0]) +
              " " + str(temp_list.get(k[0])[1]) +
              " " + str(temp_list.get(k[0])[2]))


if __name__ == "__main__":
    countries = {}
    medals = {}
    n = int(input())
    for i in range(n):
        string = input().split()
        for name in string[1:]:
            countries.update({name: string[0]})
        medals.update({string[0]: [0, 0, 0]})
    m = int(input())
    for i in range(m):
        string = input().split()
        country = countries.get(string[0])
        if int(string[1]) == 1:
            medals.get(country)[0] += 1
        elif int(string[1]) == 2:
            medals.get(country)[1] += 1
        elif int(string[1]) == 3:
            medals.get(country)[2] += 1
    print_gold(medals)
    print("-----")
    print_total(medals)
