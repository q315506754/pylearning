
# 继承与多态

class Animal(object):
    name = 'p name'
    __age = 'unkown'

    def run(self):
        print(self.__class__.__name__, 'is running...', self.name, self.__age)
        # self.name实际看子类的该属性是什么值
        # self.__age 是私有的 恒定输出unkown

    def searchFood(self):
        print(self.__class__.__name__, 'Animal不知道如何寻觅实物..')


animal = Animal()
animal.run()
print(animal)  # <__main__.Animal object at 0x0000021460DEAA58>


class Dog(Animal):
    name = 'my name is dog..'  # 继承和覆盖属性
    __age = '99 old'

    def run(self):
        print(self.__class__.__name__, '开始飞奔')

    def searchFood(self):
        super().searchFood()
        print(' 摇头摆尾乞求食物')


class Cat(Animal):

    def run(self):
        print(self.__class__.__name__, '优雅地走猫步')

    def searchFood(self):
        # super().searchFood()
        print('猫：不给不吃呗')


dog = Dog()
print(dog)  # <__main__.Dog object at 0x00000297B972A208>
cat = Cat()
print(cat)  # <__main__.Cat object at 0x00000297B972A208>

dog.run()  # Animal is running... my name is dog.. unkown
print(dog.name)  # my name is dog..

# AttributeError: 'Dog' object has no attribute '__age'
# print(dog.__age)

# 下面的访问不报错
print(dog._Animal__age)  # unkown
print(dog._Dog__age)  # 99 old

# override method
dog.searchFood()
cat.searchFood()

print(isinstance(dog, Animal))  # True
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Cat))  # False


# 重载
def run_twice(animal):
    animal.run()  # 根据实际实例的方法得到不同执行结果
    animal.run()


# 多态
run_twice(animal)  # Animal is running... p name unkown
run_twice(dog)  # Dog 开始飞奔
run_twice(cat)  # Cat 优雅地走猫步

abc = 123
# run_twice(abc) #AttributeError: 'int' object has no attribute 'run'

abc = {'run': 'aaaaa'}
# run_twice(abc) #AttributeError: 'dict' object has no attribute 'run'

abc = object()


# abc.run = 'runrun' #AttributeError: 'object' object has no attribute 'run'
# run_twice(abc) #AttributeError: 'object' object has no attribute 'run'

class Timer(object):
    def run(self):
        print('时钟滴答滴答地走...')


class Timer2(object):
    def run(self, p1):
        print('闹钟 滴答滴答地走...', p1)


# 有run方法就能调用
run_twice(Timer())  # 时钟滴答滴答地走...

# 实际调用少传了参数报错
# TypeError: run() missing 1 required positional argument: 'p1'
# run_twice(Timer2()) #

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
# 否则，将无法调用run()方法。

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：
