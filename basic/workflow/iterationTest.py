from collections import Iterable, Iterator
from enum import unique, Enum

d = {'a': 1, 'b': 2, 'c': 3}

# dict
for key in d:
    print(key)

for k, v in d.items():
    print("%s -> %s" % (k, v))

print(isinstance('abc', Iterable))  # true
print(isinstance([1, 3, 4], Iterable))  # true
print(isinstance((1, 3, 4), Iterable))  # true
print(isinstance({1, 3, 4}, Iterable))  # true
print(isinstance(111, Iterable))  # false

# 元素转换 -> 索引，元素
for i, ele in enumerate(['aaa', 222, 'bbb', True]):
    print(str(i) + " " + str(ele))

# Iterable - list、tuple、dict、set、str generator
print(Iterable)  # <class 'collections.abc.Iterable'>
print(isinstance([], Iterable))  # True
print(isinstance((x for x in range(10)), Iterable))  # True

# Iterator - generator
print(Iterator)  # <class 'collections.abc.Iterator'>
print(isinstance([], Iterator))  # False
print(isinstance(iter([]), Iterator))  # True
print(isinstance((x for x in range(10)), Iterator))  # True
it = iter([1, 3, 4])
print(it)  # <list_iterator object at 0x00000196D52E8668>


@unique
class Status(Enum):
    REQ = 1
    HLD = 2
    FIN = 3


print(Status.REQ)
print(Status.HLD)
# AttributeError: can't set attribute
# Status.REQ.value = 33

for k, v in Status.__members__.items():
    print(k, " -> ", v)

Weather = Enum('www', ('sun', 'snow', 'rain'))
for k, v in Weather.__members__.items():
    print(k, " -> ", v)

print(Weather["sun"])
print(Weather.sun)
