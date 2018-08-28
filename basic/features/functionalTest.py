from collections.abc import Iterator, Iterable
from functools import reduce


def myfunc1(n):
    print("myfunc1 invoked." + n)
    pass


# reference
a = myfunc1

# NameError: name 'function' is not defined
# print(isinstance(a,function))

print(type(a))  # <class 'function'>
print(type(myfunc1))  # <class 'function'>

a('me.')

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

print(abs)


# abs = 32


# TypeError: 'int' object is not callable
# abs(-10)

# 高阶函数
# 高阶函数英文叫Higher-order function。
#
def add(x, y, f):
    return f(x) + f(y)


def myf(x):
    return [x]


print(add(33, 22, myf))


#
#
# mr map-reduce
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)  # <map object at 0x00000198169AA080> r是一个Iterator
print(list(r))


def myd(x, y):
    return str(x) + ',' + str(y)


print(reduce(myd, [1, 3, 5, 7, 9]))

print(add(10, 20, lambda x: x * 1.234))


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# def str2float(s):
#     pass
#
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# filter
print(filter(lambda x: x is not None, ['aaa', 2323, None, 333, True, False]))  # <filter object at 0x0000021492FCD4A8>
print(list(filter(lambda x: x is not None, ['aaa', 2323, None, 333, True, False])))

print(
    list(filter(lambda x: isinstance(x, (int, float)) and x % 2 == 0, ['aaa', 2323, None, 333, 444, 666, True, False])))

aa = filter(lambda x: x is not None, ['aaa', 2323, None, 333, True, False])
print(isinstance(aa, Iterable))  # True
print(isinstance(aa, Iterator))  # True
print(next(aa))
print(next(aa))

# sorted
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
L = [36, 5, -12, 9, -21]
print("key=abs", sorted(L, key=abs))
print("key=abs,reverse=True", sorted(L, key=abs, reverse=True))
print("origin ", L)  # 排序不改变原数组

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(['Credit', 'Zoo', 'about', 'bob']))  #
