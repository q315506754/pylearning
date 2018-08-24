print([1] + [2])
print((1,) + (2, 4) + (3,))

# TypeError: can only concatenate list (not "tuple") to list
# print([1]+[2,4]+(5,6))

# TypeError: can only concatenate list (not "int") to list
# print([1]+5+[3])

# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print({1} + {3, 4} + {55} + {55})

# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print({'a':1}+{'b':1})
