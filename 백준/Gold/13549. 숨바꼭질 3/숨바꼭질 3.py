import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

maxx = 100000
dp = [float('inf') for i in range(2*maxx + 2)]
dp[n] = 0

queue = deque()
queue.append([n, 0])

while queue:
    temp, i = queue.popleft()
    if temp <= maxx and dp[temp + 1] > i + 1:
        dp[temp + 1] = min(i + 1, dp[temp + 1])
        queue.append([temp + 1, i + 1])

    if 0 <= temp - 1 and dp[temp - 1] > i + 1:
        dp[temp - 1] = min(i + 1, dp[temp - 1])
        queue.append([temp - 1, i + 1])

    if temp <= maxx and dp[temp * 2] > i:
        dp[temp * 2] = min(i, dp[temp * 2])
        queue.append([temp * 2, i])


print(dp[k])