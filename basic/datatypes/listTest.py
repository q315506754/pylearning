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

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

#出栈
classmates.pop()
print(classmates)

#删除下标对应位置的元素
classmates.pop(1)
print(classmates)

classmates.sort()
print("sort:%s"%classmates)

#不同的元素
L = ['Apple', 123, True]
print(L)

# 嵌套
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(s[2][1])

L = []
print(L)




