import datetime
n = int(input('Inserte un número: '))
i = datetime.datetime.now()
a = 0
b = 1

if n == 0:
    print(0)
elif n == 1: 
    print(1)
else:

    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    print(c)
f = datetime.datetime.now()
print(f - i)