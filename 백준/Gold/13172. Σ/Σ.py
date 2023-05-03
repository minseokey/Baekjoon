def power(num, t):
    if t == 1:
        return num % d
    elif t % 2:
        return num * power(num, t - 1) % d
    else:
        p = power(num, t // 2)
        return p * p % d

m = int(input())
d = 1000000007
ans = 0

for _ in range(m):
    n, s = map(int, input().split())
    ans += s * power(n, d - 2) % d
print(ans % d)