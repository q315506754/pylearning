from collections import Iterable, Iterator

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
print(Iterable)
print(isinstance([], Iterable))
print(isinstance((x for x in range(10)), Iterable))

# Iterator - generator
print(Iterator)
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance((x for x in range(10)), Iterator))
it = iter([1, 3, 4])
print(it)  # <list_iterator object at 0x00000196D52E8668>
