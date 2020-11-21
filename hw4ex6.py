from itertools import count
from itertools import cycle

# a)
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

# b)
a = 0
for el in cycle([1, 2, True, (2, 3), 'name']):
    if a > 10:
        break
    print(el)
    a += 1
