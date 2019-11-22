class Abc:
    def p(self):
        print("ppppp....")

    def __enter__(self):
        print("__enter__")
        # self.f = open(self.filename, 'r')

        # 这里的return 会返回给 as 后面的变量
        return self

    # return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        # self.f.close()


test = Abc()

with test as y:
    print(y)
    print(type(y))
    y.p()
