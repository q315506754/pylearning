n = 20
while n > 0:
    print(n)
    n -= 2
print('----------------')

sum = 1
while True:
    print(sum)
    sum += sum
    if sum > 1000:
        break
print('----------------')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print('----------------')

print("end")
