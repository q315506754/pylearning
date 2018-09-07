class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()


# ValueError: score must between 0 ~ 100!
# s.set_score(9999)


class Student(object):

    # 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
    # 把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def score(self):
        print('get score invoked')
        return self._score

    # @property本身又创建了另一个装饰器@score.setter
    @score.setter
    def score(self, value):
        print('set score invoked')
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
# AttributeError: 'Student' object has no attribute 'set_score'
# s.set_score(9999)
s.score = 60  # OK，实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()


class Student(object):

    #   可读写属性birth
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    #   只读属性age
    @property
    def age(self):
        return 2015 - self._birth


s = Student()
s.birth = 1990
print(s.birth)  # 1990
print(s.age)  # 25

# AttributeError: can't set attribute
# s.age=1966

s._birth = 1966
print(s.age)  # 49

# AttributeError: can't set attribute
# setattr(s,'age',999)

s.gender = 'man'
print(s.gender)

# AttributeError: 'Student' object has no attribute 'gender'
# print(Student().gender)
# AttributeError: type object 'Student' has no attribute 'gender'
# print(Student.gender)
