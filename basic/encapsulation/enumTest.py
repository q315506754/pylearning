from enum import Enum, unique

Month = Enum('Month11', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 编辑器里点不出来 但运行不报错
# print(Month.)
print(Month.Jan)

print(Month["Jan"])  # Month11.Jan
print(Month["Jan"].value)  # 1
print(Month["Feb"].value)  # 2


# KeyError: 'Febxxx'
# print(Month["Febxxx"]) #2

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    # @unique装饰器可以帮助我们检查保证没有重复值。
    Sat = 6

    # TypeError: Attempted to reuse key: 'Sat'
    # Sat = 6

    # ValueError: duplicate values found in <enum 'Weekday'>: Sat2 -> Sat
    # Sat2 = 6


print('-----------------------')
for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Weekday)  # <enum 'Weekday'>

# 可以点出来
print(Weekday.Mon)  # Weekday.Mon

print(Weekday['Mon'].value)  # 1

print(Weekday['Mon'].value == 1)  # True
print(Weekday['Mon'] == 1)  # False
# KeyError: 'Abc'
# print(Weekday['Abc']) # False
print(Weekday.Mon == 1)  # False
# AttributeError: abc
# print(Weekday.abc) # False
print(Weekday(1))  # Weekday.Mon
print(Weekday(1) == Weekday.Mon)  # True
