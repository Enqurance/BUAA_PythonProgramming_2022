for i in range(10):
    if i % 2 == 0:
        continue
    else:
        print(i, end=",")
print("He said \"Python is great\"")
print("HELLO WORLD%d''" % 3)
for s in "abc":
    for i in range(3):
        print(s * 2, end="a")
        if s == "c":
            break
print()
a = "abc"
for i in a:
    a += i
print(a)
print('abc' * 3)
b = 3
b += 2 * b
print(b)
# o = 3
# p = 4
# q = 5
# print(o ** p ** q)
# print((o ** p) ** q)
string = "abcdefghi"
print(string[3:5])
print(string[5:3:-1])
