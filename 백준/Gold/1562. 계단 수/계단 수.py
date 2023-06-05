n = int(input())
# 1차 => 비트마스크 2차 => 마지막 숫자 
dp = [[[0] * 1024 for _ in range(10)] for _ in range(n + 1)]
# dp 초기 설정
for i in range(1,10):
    dp[1][i][1<<i] = 1


for i in range(1,n):
    for j in range(10):
        for k in range(1024):
            if j == 0:
                dp[i+1][0][k | (1 << 0)] += (dp[i][1][k]% 1000000000)
            elif j == 9:
                dp[i+1][9][k | (1 << 9)] += (dp[i][8][k]% 1000000000)
            else:
                dp[i + 1][j][k | (1 << j)] += ((dp[i][j-1][k]+dp[i][j+1][k]) % 1000000000)


ans = 0
for i in range(10):
    ans += dp[n][i][-1] % 1000000000

print(ans % 1000000000)