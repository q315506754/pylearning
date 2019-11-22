s = {1, 3, 4, 4}
print(s)  # no duplicant
print(type(s))  # <class 'set'>
# s=set(1,2,3) # wrong
# print(s)
s = set([1, 2, 3, 3])
print(s)
s = set((4, 5, 6, 6))
print(s)  # just one 6
s = set((4, 5, 6, 6, (7, 8, 9), (7, 8, 9)))
print(s)  # just one (7, 8, 9)

# TypeError: unhashable type: 'list'
# s = set( [4,5,6,6,[7,8,9]])
# print(s)

s.add(99)
print(s)
s.remove(99)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # intersect
print(s1 | s2)  # union
