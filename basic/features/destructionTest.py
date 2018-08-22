import math

from basic.encapsulation.outterFunc import move

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)  # r is tuple

for x, y, z in [(1, 2, 3), (2, 3, 4), (3, 4, 5)]:
    print("%s,%s,%s" % (x, y, z))

for k, v in {'a': 23, 'b': 2323}.items():
    print(k + '=' + str(v))
