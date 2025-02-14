import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]

dp = [[-1] * n for _ in range(n)]

def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 1  # 최소 경로 길이 1
    for dy, dx in DIR:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and field[y][x] < field[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)

    return dp[y][x]


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
