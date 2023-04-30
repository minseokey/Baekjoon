n = int(input())

ans = 0
now = 64

fois = 0
while True:
    if n == ans:
        print(fois)
        break
    elif n < now:
        pass
    elif ans + now <= n:
        ans += now
        fois += 1
    now //= 2
