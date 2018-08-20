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
print([1,2,3] == True)  # X
if 1:
    print("true print")  # √
else:
    print("false print")

print([1, 2, 3] == [1, 2, 3])  # √
print([1, 2, 3] == [3, 2, 1])  # X
print([1, 2, 3] == [1, 2, 3, 4])  # X
print([1, 2, 3] == [1, 2, '3'])  # X
print([1, 2, 3] == (1, 2, 3))  # X
