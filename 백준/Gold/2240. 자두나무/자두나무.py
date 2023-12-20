import sys

t, w = map(int, sys.stdin.readline().split())

# 코인 개수별 , 좌 우별로 나누어서
dp = [[[0] * (w + 1) for _ in range(t)] for _ in range(2)]
# [][][] -> 1. 좌, 우 2. 몇번째 단계인지, 3. 코인은 몇개를 사용했는지.

now = int(sys.stdin.readline())
if now == 1:
    dp[0][0][w] = 1
else:
    dp[1][0][w-1] = 1

for time in range(1,t):
    now = int(sys.stdin.readline())
    for where in range(2):
        for coin in range(w + 1):
            # 지금 있는 자리로 자두가 떨어질때
            if now - 1 == where:
                dp[where][time][coin] = max(dp[where][time - 1][coin] + 1, dp[where][time][coin])
            else:
                # 코인 미사용
                dp[where][time][coin] = max(dp[where][time - 1][coin], dp[where][time][coin])
                # 코인 사용
                if coin != 0:
                    dp[abs(where - 1)][time][coin - 1] = max(dp[abs(where - 1)][time][coin - 1], dp[where][time - 1][coin] + 1)

ans = -1
for i in dp:
    for j in i:
        ans = max(ans,max(j))
print(ans)