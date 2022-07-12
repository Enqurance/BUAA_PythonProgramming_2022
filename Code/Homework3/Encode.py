if __name__ == "__main__":
    str_in = str(input())
    list_num = []
    for i in str_in:
        print("%03d" % ord(i), end="")
