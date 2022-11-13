n = int(input())
a = 1


def factorial(t):
    global a
    if t == 0:
        return 1
    else:
        for i in range(1, t+1):
            a = a * i
        return a


print(factorial(n))
