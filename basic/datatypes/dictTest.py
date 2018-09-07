d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])
# print(d['aab']) KeyError: 'aab'
d['Adam'] = 67
print(d)
print('Adam' in d)
print('aab' in d)
print(d.get("aab"))  # None
dx = d.get("aab")
print(dx is None)  # True
print(dx == None)  # True

print(d.get("aab", -13))  # -13  default value

print(d.pop("Bob"))  # return latest value
print(d)

e = {}
print(e)
# AttributeError: 'dict' object has no attribute 'aa'
# e.aa= 33

# print(e)
e['bb'] = 44
print(e)  # {'bb': 44}
