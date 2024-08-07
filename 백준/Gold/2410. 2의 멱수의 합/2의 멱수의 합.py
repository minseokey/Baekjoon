import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
if n == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        if i % 2 == 0:
            dp[i] = (dp[i-1] + dp[i//2]) % 1000000000
        else:
            dp[i] = dp[i-1]

    print(dp[n])
