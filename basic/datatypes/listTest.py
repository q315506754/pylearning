# list 可变顺序表
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
# print(classmates[3]) IndexError: list index out of range
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
# print(classmates[-4]) IndexError: list index out of range

# 插入 到最后
classmates.append('Adam')
print(classmates)

# 插入 到指定位置
classmates.insert(1, 'Jack')
print(classmates)

# 出栈 根据位置删除（最后一个，最顶上那个）
classmates.pop()
print("after pop:" + str(classmates))

# 根据元素值删除
classmates.remove('Bob')
print("after remove:" + str(classmates))

# 删除 根据位置删除
classmates.pop(1)
print(classmates)

classmates.sort()
print("sort:%s" % classmates)

# 不同的元素
L = ['Apple', 123, True]
print(L)

# 嵌套
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(s[2][1])

L = []
print(L)

print(['aaa',None,None,'b'])
