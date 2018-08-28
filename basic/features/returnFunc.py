def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(3, 5, 7))
print(calc_sum(3, 5, 7))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


print(lazy_sum(3, 5, 7))  # <function lazy_sum.<locals>.sum at 0x00000234EB36B620>
print(lazy_sum(3, 5, 7))  # <function lazy_sum.<locals>.sum at 0x00000234EB36B620>
print(lazy_sum(3, 5, 7) == lazy_sum(3, 5, 7))  # False


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1, f2, f3)

#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# ！！！都为9
print(f1(), f2(), f3())  # 9 9 9


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1, f2, f3)
print(f1(), f2(), f3())  # 1 4 9
