print(1 > 2)  # X
print(1 >= 2)  # X
print(1 == 1)  # √
print(1 == True)  # √
print(True is True)  # √
print(True == True)  # √
print(1 is True)  # X  ===
print(1 is not True)  # √
print(1.01 == True)  # X
print(3 == True)  # X
print(3 is True)  # X
print(0 == True)  # X
print([1, 2, 3] == True)  # X
if 1:
    print("1 true print")  # √
else:
    print("1 false print")

if 33:
    print("33 true print")  # √
else:
    print("33 false print")

if 0:
    print("0 true print")
else:
    print("0 false print")  # √

print([1, 2, 3] == [1, 2, 3])  # √
print([1, 2, 3] == [3, 2, 1])  # X 比较时考虑顺序
print([1, 2, 3] == [1, 2, 3, 4])  # X 比较时考虑集合元素幂等性

print([1, 2, 3] == [1, 2, '3'])  # X 比较时考虑类型
print([1, 2, 3] == (1, 2, 3))  # X 不可跨集合类型比较
print((1, 2, 3) == (1, 2, 3))  # √
print({1, 2, 3} == {1, 2, 3, 3})  # √ 比较时只看最终结果
print({3, 2, 1} == {1, 2, 3, 3})  # √ 比较时无视顺序
print({'a': 1, 'b': 2, 'c': 3} == {1, 2, 3})  # X
print({'a': 1, 'b': 2, 'c': 3} == {'a': 1, 'b': 2, 'c': 3})  # X
print({'a': 1, 'b': 2, 'c': 3} == {'b': 2, 'c': 3, 'a': 1})  # √ 比较时无视顺序
print({'a': 1, 'b': 2, 'c': 3} == {'b': 2, 'c': 3})  # X 比较时考虑集合元素幂等性

print(isinstance(1, (int,)))  # True
print(isinstance(1, (int)))  # True
print(isinstance(1, int))  # True
print(isinstance(1, (float)))  # False
print(isinstance(1, (bool)))  # False
print(isinstance(1, (str)))  # False

print(not True)  # False
print(not False)  # True

print("end...")  #

# 按位依次比较 若该位相等，则比较下一位，不相等时返回该位比较结果，或位数不够时直接返回false
print([1, 2, 3] < [1, 2, 3, 4])  # True
print([1, 2, 3] < [4, 1, 2, 3])  # True
print([1, 2, 3] < [4, 2, 1, 3])  # True
print([1, 2, 3] < [2, 1])  # True
print([1, 2, 3] < [2])  # True
print([1, 2, 3] < [1])  # False
print([1, 2, 3] < [1, 2, 3])  # False
print([1, 2, 3] < [1, 2, 3, 0])  # True
print([1, 2, 3] < [2, 2, 3, 0])  # True

print([1, 2, 3] > [1, 2, 2])  # True
print([1, 2, 3] > [1, 2, 3, 0])  # False
