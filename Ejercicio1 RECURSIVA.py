import datetime

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
i = datetime.datetime.now()
fibonacci(40)
f = datetime.datetime.now()
t = f - i
print(t)