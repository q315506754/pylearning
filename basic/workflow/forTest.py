print(range(5))
print(list(range(5)))  ##[0, 1, 2, 3, 4]
print(range(1, 6, 2))
print(list(range(1, 6, 2)))  # [1, 3, 5]
print('----------------')

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
    print(i)

print('----------------')

# set 循环无序
for i in {'大师傅': 323, "a": 57, "1": 43, True: "df"}:
    print(i)
