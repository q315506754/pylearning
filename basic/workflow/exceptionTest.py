g = (x for x in range(10))
print(type(g))

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
while True:
    try:
        x = next(g)
        print("x:" + str(x))
    except StopIteration as e:
        # 第一次是有值的 若不break ，后面都会是 NoneType
        print("last value:" + str(e.value))
        break

# raise TypeError
raise TypeError('aaaa has a except')
