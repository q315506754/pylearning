#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
# 否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
# 也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。


# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。
# 例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

# 一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '

__author__ = 'Michael Liao'

import sys

# import basic.encapsulation.module.moduleImport
from basic.encapsulation.module.moduleImport import *

# ['C:/pyprojects/pylearning/basic/encapsulation/module.py', 'aa', 'bb']
print(sys)
print(fABC())
print(ABC())  # <basic.encapsulation.module.moduleImport.ABC object at 0x00000212D53DA080>
print(ABC2())  # <basic.encapsulation.module.moduleImport.ABC2 object at 0x00000212D53DA080>
print(sys.argv)
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
print(sys.path)

# 如果我们要添加自己的搜索目录，有两种方法：
#
# 一是直接修改sys.path，添加要搜索的目录：
sys.path.append('/Users/michael/my_py_scripts')
print(sys.path)
# 这种方法是在运行时修改，运行结束后失效。

# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

print('module.py', __name__)  # module.py __main__


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!', args)
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!', args)


print('aaa')

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    test()


# 作用域 scope
# 有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
# private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
def _myfun1():
    print('_myfun1 private')


def __myfun1():
    print('__myfun1 private')


def ___myfun1():
    print('___myfun1 private')
