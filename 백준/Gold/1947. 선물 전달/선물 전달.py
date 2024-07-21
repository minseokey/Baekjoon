import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
if n == 1:
    print(0)
else:
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = ((i-1) * (dp[i-1] + dp[i-2])) % 1000000000
    print(dp[-1])
