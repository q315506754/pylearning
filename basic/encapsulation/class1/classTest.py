# import basic.encapsulation.class1.teacherModule

# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
# 表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
from basic.encapsulation.class1.teacherModule import Teacher


class Student(object):

    # constructor
    # 特殊方法“__init__”前后分别有两个下划线！！！
    # 但self不需要传，Python解释器自己会把实例变量传进去：
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# TypeError: __init__() missing 2 required positional arguments: 'name' and 'score'
# Student()

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
# lisa.print_score('aa')

print(bart)  # <__main__.Student object at 0x000001E9A182A080>

print()

teacher = Teacher()
print(teacher)
teacher.name = '张三'
print(teacher.name)


# 并不是NoneType
# print(teacher.age) #AttributeError: 'Teacher' object has no attribute 'age'


class Dto(object):
    a = '111'  # 实例属性
    b = 123  # 实例属性
    # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
    # 就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
    __c = '内部属性'  # 实例属性 私有  会被转化成 _Dto__c

    # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
    # 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，
    # 虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
    _d = '单个下划线可以访问'  # 实例属性

    # 内部的__name变量已经被Python解释器自动改成了 _Dto__name
    __name = None
    __score = None

    def printc(self) -> None:
        print('func访问', self.__c)

    # 如何生成getter setter?

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def set_name(self, name):
        self.__name = name


dt = Dto()
dt2 = Dto()
print(dt)  # <__main__.Dto object at 0x0000028F22E98710>
print(dt.a)  # 111
dt.a = 'changed 111'
print(dt.a)  # changed 111
print(dt2.a)  # 111

# AttributeError: 'Dto' object has no attribute '__c'
# print(dt.__c)  # 111
dt.printc()

print(dt._d)  # 单个下划线可以访问

print(dt.get_name())  # None
print(dt.get_score())  # None

__a__ = 123
print(__a__)

# 尝试修改实际内部属性
dt.set_name('set name func..')
print(dt.get_name())  # set name func..
dt._Dto__name = 'set name through _Dto__name'
print(dt.get_name())  # set name through _Dto__name  说明_Dto__name修改成功
dt.__name = 'try set __name'
print(dt.get_name())  # set name through _Dto__name   说明__name无法修改成功
print(dt.__name)  # try set __name
