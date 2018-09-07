class Student(object):
    # 类变量 共享
    pname = 'pname xx'

    def __init__(self, name):
        self.name = name


class StudentCd(Student):
    # 类变量 共享
    pname = 'StudentCd pname yy'


paren = Student('Bob')
# 实例属性
paren.score = 90
print(paren.score)

# AttributeError: type object 'Student' has no attribute 'score'
# print(Student.score)

print(Student.pname)  # pname xx
print(paren.pname)  # pname xx
print(StudentCd.pname)  # StudentCd pname yy
Student.pname = 'modified pname'
print(Student.pname)  # modified pname
print(paren.pname)  # modified pname
# 子类的变量未受影响
print(StudentCd.pname)  # StudentCd pname yy

child2 = StudentCd('zs')
# 动态添加类变量

# AttributeError: 'StudentCd' object has no attribute 'pname2'
# print(sc2.pname2)

# pname2 添加新属性
StudentCd.pname2 = 'StudentCd pname2 zz'
print(StudentCd.pname2)  # StudentCd pname2 zz

# 已经存在的实例也能访问动态创建的类变量
print(child2.pname2)  # StudentCd pname2 zz
