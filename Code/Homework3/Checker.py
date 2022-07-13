import random
import os

for i in range(100):
    f = open("input.txt", "w")
    x = random.randint(1, 5)
    y = random.randint(1, 5)
    str1 = str(x) + " " + str(y) + "\n"
    f.write(str1)
    for j in range(x):
        temp = ""
        for k in range(y):
            if k != y - 1:
                temp += str(random.randint(0, 9)) + " "
            else:
                temp += str(random.randint(0, 9))
        f.write(temp + "\n")
    f.close()
    os.system("python3 Skiing.py < input.txt > output1.txt")
    os.system("python3 CheckFile.py < input.txt > output2.txt")
    f1 = open("output1.txt")
    f2 = open("output2.txt")
    if f1.readlines() != f2.readlines():
        print("Error")
        break
    # for j in range(x):
