L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
T = ('Michael', 'Sarah', 'Tracy', 'Bob', 'Jack')

print(L[0:3])  # index [0,2]
print(L[:3])  # 如果第一个索引是0，还可以省略： index [0,2]
print(L[1:])  # index [1,最后一个]
print(L)  # 不改变数组本身
print(L[0:99])  # 超出返回全部
print(L[66:55])  # 返回[]

print(L[1:3])  # index [1,2]

print(L[-2:])  # index [倒数第二个,倒数第一个]
print(L[:-1])  # index [0,倒数第一个]
print(L[-2:-1])  # index [倒数第二个]
print(L[-2:0])  # []
print(L[-2:-0])  # []
print(L[-2:1])  # []

# 3者等效
print(L[0:100:2])  # index [0,2,4,6,8]  隔2取1
print(L[0::2])  # index [0,2,4,6,8]  隔2取1
print(L[::2])  # index [0,2,4,6,8]  隔2取1


# copy
print(L[:])

# str 是一种list
print("abcde"[:])
print("abcde"[2:])
print("abcde"[2:4])

# tuple 同 list 切片结果仍为tuple
print(T[:])
print(T[2:])
print(T[2:4])
print(T[-3:])

# print((x for x in range(10)))
# print((x for x in range(10))[:])

L = [x * x for x in range(1, 11)]
print(L)
# tuple无法使用generator生成
L = (x * x for x in range(1, 11))
print(L)
