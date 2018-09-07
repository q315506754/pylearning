class StudentNoSlot(object):
    pass


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class StudentCd(object):
    pass


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'

# AttributeError: 'Student' object has no attribute 'score'
# s.score = 99 # 绑定属性'score'

s2 = StudentNoSlot()  # 创建新的实例
s2.score = 99  # 绑定属性'score'
print(s2)  # <__main__.StudentNoSlot object at 0x000001BF767DA128>
print(s2.score)  # 99

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
s3 = StudentCd()  # 创建新的实例
s3.score = 199  # 绑定属性'score'
print(s3)  # <__main__.StudentCd object at 0x000001AD53BE84E0>
print(s3.score)  # 199
