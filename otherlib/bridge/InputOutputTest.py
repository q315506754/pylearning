birth = input('birth: ')

# TypeError: '<' not supported between instances of 'str' and 'int'
if birth < 2000:
    print('00前')
else:
    print('00后')
