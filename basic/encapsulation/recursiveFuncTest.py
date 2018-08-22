def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


for i in range(10):
    print("%s:%s" % (i, fact(i)))

# RecursionError: maximum recursion depth exceeded in comparison
# print(fact(1000))
