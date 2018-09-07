import unittest


# self.assertEqual

# with self.assertRaises(KeyError):
# value = d['empty']


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()

        # 断定有异常
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()

        # KeyError: 'empty'
        # d.empty
        # AttributeError: 'Dict' object has no attribute 'empty'

        with self.assertRaises(AttributeError):
            value = d.empty

    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

    def testok(self):
        print('testok:')

    def test_ok(self):
        print('test_ok:')

    def test_ddc(self):
        print('test_ddc:')

    # 不运行
    def Test_ok(self):
        print('test_ok:')

    def Testok(self):
        print('test_ok:')

    # 每个 !!!测试方法!!!   调用前后是否会打印出setUp...和tearDown...。
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


# 运行方式1  必须要有下面两行
if __name__ == '__main__':
    unittest.main()
# python UnitTest.py
# C:\pyprojects\pylearning\efficient\test>python UnitTest.py
# # ..test_ddc:
# # ....test_ok:
# # .testok:
# # .
# # ----------------------------------------------------------------------
# # Ran 8 tests in 0.001s


# 运行方式2
# python -m unittest UnitTest
# 结果
