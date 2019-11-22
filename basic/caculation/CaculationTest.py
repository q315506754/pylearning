print(10 / 3)
print(9 / 3)  # 整除也返回浮点型
print(10 // 3)  # 地板除

print([1] + [2, 4] + [3])

# TypeError: can only concatenate list (not "tuple") to list
# print([1]+[2,4]+(5,6))

# TypeError: can only concatenate list (not "int") to list
# print([1]+5+[3])

print((1,) + (2, 4) + (3,))

# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print({1} + {3, 4} + {55} + {55})

# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print({'a':1}+{'b':1})

a = 3
b = 4
a, b = a + b, a - b
print(a, b)
c = a + b, a - b
print(c)
print(type(c))  # <class 'tuple'>

a,b,c,d = a + b,a + b,a + b,a + b
c = a,b,c,d
print(c)
print(type(c))  # <class 'tuple'>
