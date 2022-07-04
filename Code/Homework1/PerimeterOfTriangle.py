import math

if __name__ == "__main__":
    pos_1 = input().split()
    pos_2 = input().split()
    pos_3 = input().split()
    len1 = math.sqrt(math.pow(float(pos_1[0]) - float(pos_2[0]), 2) +
                     math.pow(float(pos_1[1]) - float(pos_2[1]), 2))
    len2 = math.sqrt(math.pow(float(pos_2[0]) - float(pos_3[0]), 2) +
                     math.pow(float(pos_2[1]) - float(pos_3[1]), 2))
    len3 = math.sqrt(math.pow(float(pos_3[0]) - float(pos_1[0]), 2) +
                     math.pow(float(pos_3[1]) - float(pos_1[1]), 2))
    print("%.2f" % (len1 + len2 + len3), end="")
