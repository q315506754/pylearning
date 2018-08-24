T = (x * x for x in range(1, 4))
print(T)  # <generator object <genexpr> at 0x000001DF1DCB9390>

# TypeError: 'generator' object is not subscriptable
# print(T[0])

print(next(T))
print(next(T))
print(next(T))

# 没有更多的元素时，抛出StopIteration的错误。
# print(next(T))
print("-----------------")

T = (x for x in range(1, 10))
for x in T:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print("-----------------")
fib(6)

print("-----------------")


def fibG(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


fg = fibG(6)
print(fg)  # <generator object fibG at 0x0000022590C69390>
print("-----------------")
for x in fg:
    print(x)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
    print('step 4')


print("-----------------")
d = odd()
print(d)  # <generator object odd at 0x000001D940349480>

for x in d:
    print(x)

print("-----------------")
g = fibG(6)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
while True:
    try:
        x = next(g)
        print("x:" + str(x))
    except StopIteration as e:
        # 第一次是有值的 若不break ，后面都会是 NoneType
        print("last value:" + e.value)
        break


# 杨辉三角
def triangles():
    n = 1
    lastArr = [1]
    yield lastArr[:]

    while True:
        n += 1
        newArr = [1]

        for i in range(1, n - 1):
            newArr.insert(i, lastArr[i - 1] + lastArr[i])
            pass

        newArr.append(1)

        lastArr = newArr
        yield lastArr[:]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


def triangles2():
    L = [1]  # 初始值
    while True:
        yield (L)
        maxIndex = len(L) - 1  # 最大下标，下标从0开始
        # range(0,n)时，取的是0~(n-1)范围的数
        # 第二次获取时,len=1,range(0)=[],因此k=[],L=[1,1]
        # 第三次获取时,len=2,range(0,1)=[0],k=[2],L=[1,2,1]
        # 第四次获取时,len=3,range(0,2)=[0,1],k=[L[0]+L[1],L[1]+L[2]]]=[3,3],L=[1,3,3,1]
        k = [L[j] + L[j + 1] for j in range(maxIndex)]
        L = [1] + k + [1]


n = 0
for t in triangles2():
    print(t)
    n = n + 1
    if n == 10:
        break
