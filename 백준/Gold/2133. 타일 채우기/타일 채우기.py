import sys

n = int(sys.stdin.readline())


dp = [0 for i in range(n + 1)]
dp[0] = 1


for i in range(2,n+1):
    t = i
    ans = 0
    if t >= 2:
        ans += dp[t-2]
    while t >= 2:
        t -= 2
        ans += 2 * dp[t]

    dp[i] = ans


print(dp[n])