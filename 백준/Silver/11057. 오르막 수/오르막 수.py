import sys

n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(n)]
dp[0] = [1,1,1,1,1,1,1,1,1,1]
for i in range(1,len(dp)):
    for j in range(10):
        for k in range(j,10):
            dp[i][j] += dp[i-1][k]

print(sum(dp[-1])%10007)
