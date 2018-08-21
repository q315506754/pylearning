def calc(*numbers):
    print("len:%s" % len(numbers))
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


l = [2, 4, 6, 7, ]

# TypeError: can't multiply sequence by non-int of type 'list'
# print(calc(l))
# spread 扩展
print(calc(*l))  # len 4
