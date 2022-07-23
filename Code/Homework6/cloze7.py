def sum_all(a, b, c=100, *args, **kwargs):
    sum = a + b + c
    for d in args:
        sum += d
    print(type(kwargs))
    print(kwargs)
    for v in kwargs.values():
        sum += v
    return sum


print(sum_all(100, 200, 300, 500, 600, aa=700, bb=900, cc=1000))
print(sum_all(100, 200))
print(sum_all(100, 200, 300))
