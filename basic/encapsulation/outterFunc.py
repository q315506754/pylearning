import math


def myadd(a, b):
    return a + b


def mydivide(a, b):
    return a / b


def myempty():
    # TODO
    pass


def my_abs(x):
    print("outter my_abs")
    if x >= 0:
        return x
    else:
        return -x


def my_abs_ex(x):
    print("my_abs_ex")
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs_ex(-3))


# TypeError: bad operand type
# print(my_abs_ex('aa'))

# multi return value
def move(x, y, step, angle=0):
    # local import
    # import math
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)
print(isinstance(r, tuple))  # True
