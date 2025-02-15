import sys

n = int(sys.stdin.readline())
dp = [[0] * (100001) for _ in range(3)]
dp[0][0] = 1
dp[1][0] = 1
dp[2][0] = 1
for i in range(1, 100001):
    dp[0][i] = dp[1][i - 2]% 1000000009 + dp[2][i - 3] % 1000000009
    dp[1][i] = dp[0][i - 1]% 1000000009 + dp[2][i - 3] % 1000000009
    dp[2][i] = dp[0][i - 1]% 1000000009 + dp[1][i - 2] % 1000000009

for _ in range(n):
    t = int(sys.stdin.readline())
    print(((dp[0][t] + dp[1][t] + dp[2][t]) // 2) % 1000000009)
