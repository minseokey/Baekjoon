import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

block = defaultdict(list)
for i in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())  # y,x,y,x
    block[(a, b)].append((c, d))
    block[(c, d)].append((a, b))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][0] = 1

for summ in range(n + m + 1):
    for y in range(summ + 1):
        x = summ - y
        # 목표지점 -> y,x
        if 0 <= y <= n and 0 <= x <= m:
            if x == 0 and y == 0:
                continue
            elif y == 0:
                if (y, x) in block[(y, x - 1)] or (y, x - 1) in block[(y, x)]:
                    dp[0][x] = 0
                else:
                    dp[0][x] = dp[0][x-1]
            elif x == 0:
                if (y, x) in block[(y - 1, x)] or (y - 1, x) in block[(y, x)]:
                    dp[y][0] = 0
                else:
                    dp[y][0] = dp[y-1][0]
            else:
                if ((y, x) in block[(y, x - 1)] or (y, x - 1) in block[(y, x)]) and (
                        (y, x) in block[(y - 1, x)] or (y - 1, x) in block[(y, x)]):
                    dp[y][x] = 0
                elif (y, x) in block[(y - 1, x)] or (y - 1, x) in block[(y, x)]:
                    dp[y][x] = dp[y][x - 1]
                elif (y, x) in block[(y, x - 1)] or (y, x - 1) in block[(y, x)]:
                    dp[y][x] = dp[y - 1][x]
                else:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

print(dp[n][m])
