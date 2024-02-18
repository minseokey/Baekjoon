import sys

t = int(sys.stdin.readline())

dp = [[0] * (15) for _ in range(15)]

# init
for i in range(len(dp[0])):
    dp[0][i] = i

# dp
for i in range(1,15):
    for j in range(1,15):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    print(dp[k][n])