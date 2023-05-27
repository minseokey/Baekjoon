import sys

n = int(sys.stdin.readline())
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[None] * (1 << n) for _ in range(n)]
INF = float('inf')
ans = INF


def dfs(end, visited):
    global ans

    if visited == (1 << n) - 1:
        return lis[end][0] or INF

    if dp[end][visited] is not None:
        return dp[end][visited]

    temp = INF

    for i in range(n):
        if visited & (1 << i) == 0 and lis[end][i] != 0:
            temp = min(temp, dfs(i, visited | (1 << i)) + lis[end][i])
    dp[end][visited] = temp
    return temp


print(dfs(0, 1))
