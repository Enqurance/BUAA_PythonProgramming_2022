if __name__ == "__main__":
    a = input()
    b = input()
    stack = ""
    while True:
        put = a[0]
        pos = stack.find(put)
        if pos >= 0:
            stack += put
            a += stack[pos:]
            stack = stack[:pos]
        else:
            stack += put
        a = a[1:]
        if len(a) == 0:
            break
        put = b[0]
        pos = stack.find(put)
        if pos >= 0:
            stack += put
            b += stack[pos:]
            stack = stack[:pos]
        else:
            stack += put
        b = b[1:]
        if len(b) == 0:
            break
    if len(b) == 0:
        print("Hahaha~")
        print(a)
    else:
        print("Oh, no!")
        print(b)
