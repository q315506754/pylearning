def addToList(str, l=[]):
    l.append(str)
    print(l)


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
addToList("aa")  # ['aa']
addToList("aa")  # ['aa', 'aa']
addToList("aa")  # ['aa', 'aa', 'aa']


# 修改版
def add_end(str, L=None):
    if L is None:
        L = []
    L.append(str)
    print(L)
    return L


add_end("aa")  # ['aa']
add_end("aa")  # ['aa']
add_end("aa")  # ['aa']
