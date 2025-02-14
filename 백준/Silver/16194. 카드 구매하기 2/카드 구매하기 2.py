import sys

n = int(sys.stdin.readline())
prices = [0] + list(map(int,sys.stdin.readline().split()))

dp = [float('inf')] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        dp[j] = min(dp[j], dp[j-i] + prices[i])

print(dp[-1])
