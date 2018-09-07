class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Michael'))  # <__main__.Student object at 0x0000019D9F744FD0>


class Student(object):
    def __init__(self, name):
        self.name = name

    # 重写 toString
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # __repr__()返回程序开发者看到的字符串
    # repl环境
    def __repr__(self):
        return 'Student object (name: %s)' % self.name

    # 有个偷懒的写法：
    __repr__ = __str__


print(Student('Michael'))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
    # Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
    # 直到遇到StopIteration错误时退出循环。
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 1000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)

l = list(Fib())
print(l)


# print(Fib()[5])  # TypeError: 'Fib' object does not support indexing

class Fib(object):
    def __getitem__(self, n):
        print(type(n))
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


print(Fib()[5])  # 8
print(Fib()[0])  # 1
print(Fib()[-1])  # 1


# print(list(Fib())[5:10]) # dead cycle
# print(Fib()[5:10]) #TypeError: 'slice' object cannot be interpreted as an integer

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            print('instance(n, int)')
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            print('instance(n, slice)')
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


print(Fib()[5:10])
print(Fib()[:10])


class Student(object):

    def __init__(self):
        self.name = 'Michael'


# print(Student().aa) #AttributeError: 'Student' object has no attribute 'aa'

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'aa':
            return 99

        # 可以返回函数
        if attr == 'age':
            return lambda: 25

        # raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# 当调用不存在的属性时，比如score，
# Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
print(Student().aa)  # 99
print(Student().bb)  # None  不报错了
print(Student().__getattr__('score'))  # None  不报错了
print(Student().__getattr__('aa'))  # 99

print(Student().age())  # 25


# 应用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


# invoke instance
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()  # My name is Michael.

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
# 所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

print(callable(Student('Michael')))  # True
print(callable(max))  # True
print(max.__call__)  # <method-wrapper '__call__' of builtin_function_or_method object at 0x000001CA203D9678>
print(callable(None))
print(callable(1))
print(callable([1, 2, 3]))
