import functools

print(int('12345', base=8))
print(int('12345', base=16))
print(int('FFFF', base=16))  # 65535

# 三进制
print(int('1122111', base=3))  # 1201


# print(int('12345', base=2)) #invalid literal for int() with base 2: '12345'


def int2(x, base=2):
    return int(x, base)


print(int2('101000101'))
print(int2('11111111'))  # 255

# ，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
int3 = functools.partial(int, base=2)
print(int3('101000101'))
print(int3('11111111'))  # 255

# *args
max2 = functools.partial(max, 10, 100, 1000)
print(max2(101, 202, 1, 5))  # 1000
