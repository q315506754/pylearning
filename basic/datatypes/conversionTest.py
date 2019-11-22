classmates = ['Michael', 'Bob', 'Tracy']
obj = {'a': 23, "b": 4}
bl = True
# TypeError: can only concatenate str (not "type") to str
# print("list:"+list)

# TypeError: can only concatenate str (not "dict") to str
# print("obj:"+obj)

# TypeError: can only concatenate str (not "bool") to str
# print("bl:"+bl)
print("bl:" + str(bl))

d = str(obj)
print(d)

d2 = "".join(obj)
print(d2) #{'a': 23, 'b': 4}
d2 = "".join(classmates)
print(d2)  #ab
d2 = "-".join (obj)
print(d2) #a-b
d2 = "-".join(classmates)
print(d2) #Michael-Bob-Tracy

# birth = input('birth: ')
birth = '1987'

# TypeError: '<' not supported between instances of 'str' and 'int'
# if birth < 2000:

if int(birth) < 2000:
    print('00前')
else:
    print('00后')

# str,float,bool -> int
print(int('123'))  # 123
print(int(12.34))  # 12
print(int(True))  # 1
print(int(False))  # 0
print("------------------")

# str,int,bool -> float
print(float('12.34'))
print(float(True))  # 1.0
print(float(False))  # 0.0
print("------------------")

# any ->str
print(str(1.23))
print(str(100))
print("------------------")
# str,float,int ->bool
print(bool(1))  # True
print(bool(33))  # True
print(bool(''))  # False
print(bool('123'))  # True
print(bool('0'))  # True
print(bool(int('0')))  # False
print(bool(float('0')))  # False
print(bool(0))  # False
print(bool(-1))  # True
print(bool(0.01))  # True
print("------------------")
