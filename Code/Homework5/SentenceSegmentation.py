if __name__ == "__main__":
    str1 = str(input())
    str2 = str(input())
    str3 = str2.lower()
    result = ""
    while True:
        p = str3.find(str1.lower())
        temp = ""
        if p < 0:
            result += str2 + " "
            break
        if p == 0:
            for i in range(len(str1)):
                temp += str2[i]
            str2 = str2[len(str1):]
            str3 = str3[len(str1):]
        else:
            for i in range(p):
                temp += str2[i]
            str2 = str2[p:]
            str3 = str3[p:]
        result += temp + " "
    result = result[:len(result) - 1]
    print(result)
