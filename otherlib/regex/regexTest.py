import re

m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
print(m.group(0))

# 零宽断言  前，后
m = re.search('(?<=www\.).*(?=\.com)', 'https://www.runoob.com/python/python-reg-expressions.html')
m.group(0)
print(m.group(0))