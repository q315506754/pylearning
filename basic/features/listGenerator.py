import os

print(list(range(1, 11)))  # 1~10

L = [x * x for x in range(1, 11)]
print(L)

print([x + x for x in range(1, 11)])
print([x % 2 == 0 for x in range(1, 11)])
print([x for x in range(1, 11, 2)])
print([x.lower() for x in "ABCD"])  # ['a', 'b', 'c', 'd']

# if condition
print([x for x in range(1, 11) if x % 2 == 0])

# double cycle n为内层
print([m + n for m in 'ABC' for n in 'XYZ'])

# 3层循环 由外及内
print([m + n + k for m in 'ABC' for n in 'XYZ' for k in '123'])

print(os.listdir('.'))
print([d for d in os.listdir('.')])

# 多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
