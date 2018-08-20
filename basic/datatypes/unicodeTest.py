#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: gbk -*-
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

print('包含中文的str')

a = ord('A')
print(a)
a = chr(25991)
print(a)
a = '\u4e2d\u6587'
print(a)
a = 'ABC'
print(a)
a = b'ABC'
print(a)
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# print( '中文'.encode('ascii'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len(b'ABC'))
print(len('中文'))

# 计算字节数
print(len('中文'.encode('utf-8')))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

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

# 格式化2
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
