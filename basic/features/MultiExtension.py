class Animal(object):
    pass


####行为
class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 大类:
#  哺乳动物  /'mæm(ə)l/
class Mammal(Animal):
    def produce(self):
        print('胎生...')

    pass


class Bird(Animal):
    def produce(self):
        print('卵生...')

    pass


# 各种动物:
# 这种 多重继承 设计通常称之为MixIn。
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# Mammal 和 Bird都有  produce 方法，这里由于先继承的Mammal，调用的是Mammal的produce方法
class Alien(Mammal, Bird, Runnable, Flyable):
    pass


d = Dog()
print(d)
d.produce()
d.run()

b = Bat()
print(b)
b.produce()
b.fly()

a = Alien()
print(a)
a.produce()
a.fly()
