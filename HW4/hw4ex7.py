def fact(x):
    if x == 0:
        yield 1
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a

for x in fact(4):
    print(x)
