# 格式化1
a = 'Hello, %s' % 'world'
print(a)
a = 'Hello, %x' % 0xFFFF
print(a)
a = 'Hello, %d' % 0xFFFF
print(a)
a = 'Hello, %x' % 66666
print(a)
a = 'Hello, %d' % 66666
print(a)
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
a = 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print(a)

print('Age: %s. Gender: %s' % (25, True))

print('growth rate: %d %%' % 7)

# TypeError: %d format: a number is required, not str
# print('growth rate: %d %%' % str(7))
print('growth rate: %s %%' % str(7))

# 格式化2
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
