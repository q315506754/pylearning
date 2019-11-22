# 整数
a = 1
print(a)
a = -1
print(a)
a = 0xff00
print(a)
a = 0xa5b4c3d2323
a = 0xa5b4c3d2323df4343443434
print(a)
print("------------------")

# 浮点数
b = 1.23
print(b)
b = -9.01
print(b)
b = 1.23e9
print(b)
b = 1.2e-5
print(b)
print("------------------")

# 字符串
c = "abc"
print(c)
c = 'abc'
print(c)
c = 'a"b"c'
print(c)
c = "a'b'c"
print(c)
# # escape
c = 'a\'b\'c'
print(c)
c = '\t\t\thaha'
print(c)
c = r'\t\t\thaha'  # 不转义
print(c)
c = '''aaa
bbb
ccc'''
print(c)
c = 'aaa' \
    'bbb' \
    'ccc'
print(c)  # 字符串换行

# 拼接字符串
d = c + c + c
print(d)

print("------------------")

# bool值
d = True
print(d)
d = False
print(d)
print("------------------")

# null值
e = None
print(e)
print("------------------")

# 常量
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，
# 所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
PIX = 3141514
print(PIX)
PIX = 3.2323
print(PIX)
print("------------------")

a = 'abcabcbca'
print(a.replace('a', 'A'))
print(a)
print("------------------")

# trim
print('  '.strip())
print('  A'.strip())
print('  A   B'.strip())
print('  A   B   '.strip())
