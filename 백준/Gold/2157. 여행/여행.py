import sys

n, m, k = map(int, sys.stdin.readline().split())
m -= 1

path = [[0] * n for _ in range(n)]

for _ in range(k):
    a, b, w = map(int, sys.stdin.readline().split())
    if a < b:
        path[a - 1][b - 1] = max(path[a - 1][b - 1], w)

dp = [[-1] * (m + 1) for _ in range(n)]
dp[0][0] = 0

for t in range(1, m + 1):
    for fr in range(n):
        for to in range(fr+1, n):
            if path[fr][to] != 0 and dp[fr][t-1] != -1:
                dp[to][t] = max(dp[to][t], dp[fr][t-1] + path[fr][to])


print(max(dp[-1]))
