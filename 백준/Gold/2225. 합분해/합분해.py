import sys

n,k = map(int,sys.stdin.readline().split())

# 0~n 까지 정수를  k 개 더해서 그 합을 n 이 되게 하는 방법 수

dp = [[0] * k for i in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(k):
    dp[0][i] = 1

for i in range(1,n+1):
    for j in range(1,k):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000000

print(dp[-1][-1])