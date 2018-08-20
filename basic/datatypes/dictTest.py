d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])
# print(d['aab']) KeyError: 'aab'
d['Adam'] = 67
print(d)
print('Adam' in d)
print('aab' in d)
print(d.get("aab"))
print(d.get("aab", -13))

print(d.pop("Bob")) # return latest value
print(d)
