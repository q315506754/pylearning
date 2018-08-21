# tuple 元组
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

print(classmates[1])

# classmates[0] = 'dsfsfd' TypeError: 'tuple' object does not support item assignment

# classmates.__add__(("aa",))
# print(classmates)

# 歧义
t = ()  #
t = (1)  # 此时t为1 Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
print(t)
t = (1,)  # 消除歧义 Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
print(t)
print(len(t))

# “可变的”tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
