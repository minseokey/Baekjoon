n = int(input())


def fibonacci(t):
    if t == 0:
        return 0
    if t == 1:
        return 1
    return fibonacci(t - 2) + fibonacci(t - 1)


print(fibonacci(n))
