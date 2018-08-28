import functools
import time


def now():
    print('2015-3-25')


now()
f = now
print(now.__name__)
print(now.__class__)
print(now.__code__)


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# Proxy 代理

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
    def wrapper(*args, **kw):
        print('--wrapper--call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


N = log(now)
N()


# 中间有任意空行都可以 相当于
# myfunclog = log(myfunclog)
@log
def myfunclog():
    print(__name__, " invoked.")
    # 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
    print(myfunclog.__name__, " invoked.")  # wrapper  invoked.


#     因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。


myfunclog()


# 带参数的decorator
def logWithParam(p1, p2):
    def deco(func):
        def wrapper(*args, **kw):
            print('--logWithParam--call %s(): %s(): %s():' % (func.__name__, p1, p2))
            return func(*args, **kw)

        return wrapper

    return deco


# myfunclog2 = logWithParam('execute')(myfunclog2)
@logWithParam("p1p1", "ppp2")
def myfunclog2():
    print("myfunclog2 invoked...")


myfunclog2()

N2 = logWithParam("p1p11111", "ppp22222")(lambda x: print('lambda print:%s' % x))
print(N2)
N2(23)


# 继承原函数名字
def log3(func):
    # 继承原函数名字 core
    @functools.wraps(func)
    def wrapper3(*args, **kw):
        print('--wrapper3--call %s():' % func.__name__)
        rt = func(*args, **kw)

        print('#rt', rt)  # rt None
        # AttributeError: 'NoneType' object has no attribute '__name__'
        # rt.__name__ = func.__name__

        return rt

    return wrapper3


def mylog3():
    print('mylog3...')


mylog3()
print('mylog3.__name__', mylog3.__name__)  # mylog3.__name__ mylog3

mylog3 = log3(mylog3)
print('mylog3.__name__', mylog3.__name__)  # mylog3.__name__ mylog3

mylog3()


# test
def metric(fn):
    @functools.wraps(fn)
    def wrapperTest(*args, **kw):
        stt = time.clock()
        rt = fn(*args, **kw)
        cost = time.clock() - stt
        print('%s executed in %s ms' % (fn.__name__, cost))
        return rt

    return wrapperTest


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
