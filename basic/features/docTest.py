import re

m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
print(m.group(0))

'''
fdfdsfds
'''

# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.get('x')
    100
    >>> d1['x']
    100
    >>> 'x' in d1
    True
    >>> 'x22' in d1
    False
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2['c']
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'

    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    # def __getattr__(self, key):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# ide环境下直接运行即可
# import doctest
# doctest.testmod()

# 防误执行测试代码
if __name__ == '__main__':
    import doctest

    doctest.testmod()
