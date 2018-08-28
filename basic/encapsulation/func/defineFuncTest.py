from basic.encapsulation.func.outterFunc import myadd, mydivide, myempty
from basic.encapsulation.func.outterFunc2 import *

# from basic.encapsulation.outterFunc import *
# from basic.encapsulation.outterFunc import *
# from basic.encapsulation.outterFunc import *


myadd222()


# this import will cause script to be invoked
# 无论是* 还是 myadd, mydivide,myempty，都导致 __init__.py invoked
# 同一个包下引入两个的方法，这个包下 __init__.py 只执行一次
# 就算只引入一部分方法也会让其它脚本执行
# from basic.encapsulation.outterFunc import myadd, mydivide,myempty

def my_abs(x):
    print("inner my_abs")
    if x >= 0:
        return x
    else:
        return -x


# inner my_abs first
print(my_abs(-23))
print(my_abs(23))


# 可重复定义
def my_abs(x):
    return


print(my_abs(-23))  # None
print(my_abs(23))  # None

# import func
print(myadd(2, 3))
print(mydivide(2, 3))

# ZeroDivisionError: division by zero
# print(mydivide(2,0))

myempty()


# 函数参数类型
# 正常定义的必选参数外
# 还可以使用默认参数、
# 可变参数和
# 关键字参数

# 正常
def power(x):
    print("overload 1")
    return x * x


# 默认参数 函数覆盖掉前面定义的了
def power(x, n=2):
    print("overload 2")
    i = 0
    sum = 1
    while i < n:
        sum *= x
        i += 1
    return sum


print(power(15))
print(power(15, 3))


# compile error
# 非默认参数不能跟在默认参数后面
# def defaultPFunc(a=2,b,c):

def pList(l=[]):
    for i in l:
        print(i)


pList([1, 2, 3])  # ok
pList((1, 2, 3))  # ok
pList({'a': 3, 'b': 44})  # ok


# TypeError: 'NoneType' object is not iterable
# pList(None)#wrong

# 可变参数
def calc(*numbers):
    print("len:%s" % len(numbers))
    print("str:%s" % str(numbers))
    print("is tuple:%s" % isinstance(numbers, tuple))
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(2, 4, 2, 3, 6))
print(calc(2, 4, 2, 3, 6))
print(calc())  # len 0
l = [2, 4, 6, 7, ]

# no such st
# def calc2(*numbers=[]):

# TypeError: can't multiply sequence by non-int of type 'list'
# print(calc(l))
# spread 扩展
print(calc(*l))  # len 4


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


def person2(name, age, **kw22):
    print("kw22:" + str(kw22))
    print("is dict:" + str(isinstance(kw22, dict)))

    # TypeError: 'gender' is an invalid keyword argument for str()
    # print("kw22:" + str(**kw22))

    print('name:', name, 'age:', age, 'other:', kw22)


person('Michael', 30)
person2('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person2('Jack', 24, city2=extra['city'], job2=extra['job'])
person2('Jack', 24, **extra)


# TypeError: person2() argument after ** must be a mapping, not list
# person2('Jack', 24, **l)


# 命名关键字参数
# 限制关键字参数的名字
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24, job='Engineer', city='Beijing')  # 顺序换过来也ok
# person('Jack', 24, job='Engineer', city='Beijing', city2='Beijing2') # 多了不行 TypeError: person() got an unexpected keyword argument 'city2'
# person('Jack', 24, job='Engineer') # 少了也不行 TypeError: person() missing 1 required keyword-only argument: 'city'

# TypeError: person() takes 2 positional arguments but 4 were given
# person('Jack', 24, 'Beijing', 'Engineer')

# TypeError: person() takes 2 positional arguments but 3 were given
# person('Jack', 24, {'city': 'Beijing', 'job': 'Engineer'})

# 可以用关键字参数的**解开
person('Jack', 24, **{'city': 'Beijing**', 'job': 'Engineer**'})


# TypeError: 'city' is an invalid keyword argument for print()
# print( **{'city': 'Beijing**', 'job': 'Engineer**'})

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person('Jack', 24, job='Engineer')


# TypeError: person() missing 1 required keyword-only argument: 'job'
# person('Jack', 24)


# 参数组合
# 在Python中定义函数，
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


def f3(a, b, c=0, *args, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'd =', d, 'kw =', kw)


#     错误定义
# def f3(a, b, c=0, *args,**kw,d):
#     print('a =', a, 'b =', b, 'c =', c, 'args =',args, 'd =', d, 'kw =', kw)
#     错误定义
# def f3(a, b, c=0,  **kw,*args):
#     print('a =', a, 'b =', b, 'c =', c, 'args =',args, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, 4, 4, 4)
f1(1, 2, 4, 4, 4, aa=1, bb=2, cc=3)
f1(1, 2, 4, 4, 4, df=1, bb=2, cc=3)
f2(1, 2, d=99, ext=None)
# f2(1, 2, 3,4,d=6)
f2(1, 2, 3, d=6)

args = (1, 2, 3, 4, 5, 6)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

f2(*(4, 5, 6), **kw)
