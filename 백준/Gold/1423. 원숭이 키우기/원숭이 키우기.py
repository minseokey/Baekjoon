import sys

n = int(sys.stdin.readline())
lev = [0] + list(map(int, sys.stdin.readline().split()))
power = [0] + list(map(int, sys.stdin.readline().split()))
d = int(sys.stdin.readline())

summ = sum(lev[i] * power[i] for i in range(n+1))

for i in range(n):
    lev[i] = min(d, lev[i])

dp = [0] * (d + 1)
for i in range(1, n+1):
    while lev[i] > 0:
        lev[i] -= 1
        for j in range(d, -1, -1):
            for k in range(i + 1, n + 1):
                if k + j - i <= d:
                    dp[k + j - i] = max(dp[k + j - i], dp[j] + power[k] - power[i])

print(dp[d] + summ)