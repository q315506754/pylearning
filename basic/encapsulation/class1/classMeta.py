from basic.encapsulation.class1.teacherModule import Teacher

#动态创建类、元类、继承、类共享字段


a = Teacher()
print(a)
print(a.__class__)  # <class 'basic.encapsulation.class1.teacherModule.Teacher'>
print(type(a))  # <class 'basic.encapsulation.class1.teacherModule.Teacher'>


def func():
    pass


print(type(func))  # <class 'function'>

# 拿到type可以直接new出新对象来
aa = type(a)()  # <basic.encapsulation.class1.teacherModule.Teacher object at 0x0000017AC3FCA0B8>
print(aa)
aa.say()


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


print(dict(hello=fn))
print(dict(aaa=111, bbb=222))
# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
print(Hello)  # <class '__main__.Hello'>
Hello().hello()  # Hello, world.
Hello().hello(' kk')  # Hello,  kk.


# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
#
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，
# 必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

# metaclass
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    # 当前准备创建的类的对象；
    # 类的名字；
    # 类继承的父类集合；
    # 类的方法集合。
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        # <class '__main__.ListMetaclass'>
        # MyList
        # (<class 'list'>,)
        # {'__module__': '__main__', '__qualname__': 'MyList'}

        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


print(type)  # <class 'type'>

# TypeError: object.__new__(): not enough arguments
# print(Hello.__new__())
print(Hello.__new__)  # <built-in method __new__ of type object at 0x00007FFA58D08EC0>


# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
# ，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
class MyList(list, metaclass=ListMetaclass):
    pass


l = MyList()
l.add("aa")
l.add("bb")
print(l)

L2 = list()


# AttributeError: 'list' object has no attribute 'add'
# L2.add("bb")


class Field(object):

    # 构造函数
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    # toString
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


print(IntegerField('age'))


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):

        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found model: %s' % name)
        print('attrs : %s' % attrs)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，
# 如果没有找到，就继续在父类Model中查找metaclass，
# 找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，
# 也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

print(u.id)  # 12345
u.id = 23456
print(u.id)  # 23456

# AttributeError: type object 'User' has no attribute 'id'
# print(User.id)

u2 = User(id=333444, )
print(u2.id)  # 333444
print(u.id)  # 23456


# print(u.iddd)

class Student(object):
    # 类变量 共享
    pname = 'pname xx'

    def __init__(self, name):
        self.name = name


print(Student.pname)  # pname xx
# print(Student().pname)

# AttributeError: type object 'User' has no attribute 'name'
# print(User.name)
