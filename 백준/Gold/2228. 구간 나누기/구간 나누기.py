import sys

n, m = map(int, sys.stdin.readline().split())
lis = [int(sys.stdin.readline()) for _ in range(n)]

dp = [[[-float('inf')] * m for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i][0] = lis[i]
    for j in range(i + 1, n):
        dp[i][j][0] = dp[i][j-1][0] + lis[j]


for k in range(1, m):
    for i in range(n):
        for j in range(i, n):
            if j >= i + 2:
                temp = -float('inf')
                for t in range(j-1):
                    temp = max(temp, dp[i][t][k-1])
                dp[i][j][k] = max(temp + lis[j], dp[i][j][k], dp[i][j-1][k] + lis[j])

maxx = -float('inf')
for i in dp:
    for j in i:
        maxx = max(maxx, j[-1])

print(maxx)