a = [1, 2, 3, 4, 5]
b = a
c = a.copy()
print(a)
print(b)
print(c)
a.append(6)
print(a)
print(b)
print(c)
d = [4, 5]
e = [1, 2, 3, d]
f = e.copy()
print(e)
print(f)
e.append(6)
print(e)
print(f)
d.append(7)
print(e)
print(f)
