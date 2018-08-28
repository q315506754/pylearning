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
print('----------------')

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# unicode(Memory)  encode -> bytes(File)
# bytes(File)  decode -> unicode(Memory)
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# print( '中文'.encode('ascii'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len(b'ABC'))  # 3
print(len('中文'))  # 2

print('----------------')
# 计算字节数
print(len('中文'.encode('utf-8')))  # 6
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 6

print(isinstance('中文'.encode('utf-8'), bytes))  # true
print(isinstance('中文'.encode('utf-8'), str))  # False
