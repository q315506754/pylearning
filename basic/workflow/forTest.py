print(range(5))
print(list(range(5)))  ##[0, 1, 2, 3, 4]
print(range(1, 6, 2))
print(list(range(1, 6, 2)))  # [1, 3, 5]
print('----------------')

print(type(range(1, 6, 2)))

for i in range(1, 6, 2):
    print(i)
print('----------------')

for i in (1, 3, 5, 6):
    print(i)

print('----------------')

for i in [1, 3, 5, 6]:
    print(i)

print('----------------')

# set 循环无序
for i in {6, 1, 3, 3, 4}:
    print(i)  # 1 3 4 6

print('----------------')

# dict
for i in {'大师傅': 323, "a": 57, "6": 43, "1": 23, "2": 434, True: "df"}:
    print(i)  # 这里按顺序输出的 为什么
for i,j in {'大师傅': 323, "a": 57, "6": 43, "1": 23, "2": 434, True: "df"}.items():
    print(i,"=",j)  # 这里按顺序输出的 为什么
