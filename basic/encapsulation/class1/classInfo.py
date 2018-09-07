def myf():
    pass


class Abc:
    abc = 'asddsds'
    pass


print(type(123))  # <class 'int'>
print(type(abs))  # <class 'builtin_function_or_method'>
print(type(myf))  # <class 'function'>
print(type(Abc))  # <class 'type'>
print(Abc.__class__)  # <class 'type'>
print(type(object))  # <class 'type'>
print(type(Abc()))  # <class '__main__.Abc'>
a = Abc()
print(a.__class__)  # <class '__main__.Abc'>

# logic
print(type(123) == type(456))  # True
print(type(123) == type('123'))  # False
print('--------------------')

# inheritance
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance(Abc, object))  # True
print(isinstance(Abc(), object))  # True
print(isinstance(Abc(), Abc))  # True
print(isinstance(Abc, Abc))  # False

# TypeError: isinstance() arg 2 must be a type or tuple of types
# print(isinstance(Abc(),Abc())) #TypeError: isinstance() arg 2 must be a type or tuple of types

print(dir(
    Abc))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'abc']
print(dir(Abc()))  # 同上
print(
    Abc.__dict__)  # {'__module__': '__main__', 'abc': 'asddsds', '__dict__': <attribute '__dict__' of 'Abc' objects>, '__weakref__': <attribute '__weakref__' of 'Abc' objects>, '__doc__': None}
print(a.__dict__)  # {}


# print(len(a)) #TypeError: object of type 'Abc' has no len()

class MyLen:
    a = '123'
    _a = '234'
    __a = '345'

    __a__ = '456'

    __a_ = '567'

    def __len__(self):
        return 33


# TypeError: object of type 'type' has no len()
# print(len(MyLen))

print(len(MyLen()))  # 33

# introspect
print(getattr(MyLen(), 'a'))  # 123
print(getattr(MyLen(), '_a'))  # 234

# AttributeError: 'MyLen' object has no attribute '__a'
# print(getattr(MyLen(),'__a'))
print(getattr(MyLen(), '_MyLen__a'))  # 345

print(getattr(MyLen(), '__a__'))  # 456
print(MyLen().__a__)  # 456

# AttributeError: 'MyLen' object has no attribute '__a_'
# print(getattr(MyLen(),'__a_'))#456
print(getattr(MyLen(), '_MyLen__a_'))  # 567

ml = MyLen()
setattr(ml, 'a', '%123')
print(ml.a)  # %123

setattr(ml, '_a', '%234')
print(ml._a)  # %123

setattr(ml, '__a', '%345')
print(ml.__a)  # %345
print(ml._MyLen__a)  # 345

print(hasattr(ml, '__len__'))  # True
print(hasattr(ml, '__a'))  # True
print(hasattr(ml, '__ab'))  # False

print(ml.__len__)  # <bound method MyLen.__len__ of <__main__.MyLen object at 0x00000207D1C08A58>>
setattr(ml, '__len__', lambda: 'aab len')
print(len(MyLen()))  # 33
print(len(ml))  # 33   ???
print(ml.__len__)  # <function <lambda> at 0x000002467438B620>
print(ml.__len__())  # aab len
print(MyLen().__len__())  # 33


def mylength(self):  # 定义一个函数作为实例方法
    return 123312


from types import MethodType

# 给实例绑定一个方法
# 尝试给实例绑定一个方法：
ml.__len__ = MethodType(mylength, ml)
print(ml.__len__)  # <bound method mylength of <__main__.MyLen object at 0x000002B2231E8A90>>
print(ml.__len__())  # 123312
print(MyLen().__len__())  # 33
print(len(ml))  # 33

# 绑定到类上 实例也可使用动态方法 包括已经存在的实例
MyLen.dfunc = MethodType(mylength, ml)
print(MyLen.dfunc)  # <bound method mylength of <__main__.MyLen object at 0x0000027536268AC8>>
print(MyLen.dfunc())  # 123312
print(MyLen().dfunc())  # 123312
print(ml.dfunc())  # 123312

MyLen.dfunc2 = mylength
print(MyLen.dfunc2)  # <function mylength at 0x00000258C93DB730>
# print(MyLen.dfunc2()) # TypeError: mylength() missing 1 required positional argument: 'self'
print(MyLen().dfunc2())  # 123312
print(ml.dfunc2())  # 123312
