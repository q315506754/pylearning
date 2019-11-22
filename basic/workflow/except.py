import logging
# from logging import *

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    # e.with_traceback()
    print('except:', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    # 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
    print('no error!')
finally:
    print('finally...')
print('END')


# err.py:
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()

def main():
    try:
        bar('0')
    except Exception as e:
        print('logging.exception(e)')

        # 多了一行
        # ERROR:root:division by zero
        # Traceback (most recent call last):
        # File "C:/pyprojects/pylearning/basic/workflow/except.py", line 57, in main
        #   bar('0')
        # File "C:/pyprojects/pylearning/basic/workflow/except.py", line 48, in bar
        #   return foo(s) * 2
        # File "C:/pyprojects/pylearning/basic/workflow/except.py", line 45, in foo
        #   return 10 / int(s)
        # ZeroDivisionError: division by zero
        logging.exception(e)
        # exception(e)


# Python内置的logging模块可以非常容易地记录错误信息：
# main()

print('end，')


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

        # 可以换一种错误类型抛出
        # raise ValueError('input error!')


# bar()

# AssertionError
#     可以捕获异常
#     ，启动Python解释器时可以用-O 大写的欧 参数来关闭assert：
# try:
assert 1 == 0
assert 1 == 0
assert 1 == 0
print('-----aaa')
assert 1 == 0
print('-----bbbb')
assert 1 == 0
# except:
#     pass


print('end......')

s = '0'
n = int(s)
print('n = %d' % n)

# 有debug，info，warning，error等几个级别
logging.basicConfig(level=logging.INFO)
# INFO:root:n = 0 加了才会输出

logging.info('n = %d' % n)

print(10 / n)
