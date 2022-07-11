for i in range(1900, 2023):
    if i % 400 == 0 or (i % 100 != 0 and i % 4 == 0):
        print(i)
    else:
        continue
        print(i)
