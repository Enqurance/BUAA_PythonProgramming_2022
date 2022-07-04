from variable import pi
import math

if __name__ == "__main__":
    print("Hello, this is the entrance:")
    lst = map(float, input("Please input the radius:").split())
    for item in lst:
        print(pi * math.sqrt(item))
