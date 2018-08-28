L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)

f = lambda x: x * x
print(f)  # <function <lambda> at 0x0000021CCD89C268>


def build(x, y):
    return lambda: x * x + y * y


print(build(3, 5))  # <function build.<locals>.<lambda> at 0x0000021CCF54B620>
