n = int(input())
k = int(input())

# N 을 선택하지 않았을때 -> 1 ~ N-1 (k)
# N 을 선택했을때 -> 2 ~ N-2 (k-1)

dp = [[0] * (k + 1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1

for i in range(2, n+1):
    for j in range(1, k+1):
        dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % 1_000_000_003
    
print((dp[n][k] + dp[n-2][k-1]) % 1_000_000_003)
