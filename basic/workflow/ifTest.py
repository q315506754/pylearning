age = 20
if age >= 18:
    # 4个空格 =  1个tab
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

    print('teenager2')
print('out。。')
# print('teenager2') #compile error

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

age = 20
if age >= 6:
    print('teenager')
#     把该判断对应的语句执行后，就忽略掉剩下的elif和else
elif age >= 18:
    print('adult')
else:
    print('kid')

print('end。。')
