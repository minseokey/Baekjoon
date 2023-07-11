import sys

n = int(input())
MOD = 1000000009
dp = [0, 1, 2, 4]
for _ in range(n):
    target = int(input())

    if target < len(dp) - 1:
        print(dp[target])
    else:
        for i in range(len(dp), target+1):
            dp.append((dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD)

        print(dp[target])
