import heapq
import sys

n = int(sys.stdin.readline())
start = tuple(map(int, sys.stdin.readline().split()))
lis = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[float('inf')] * 5 for _ in range(n + 1)]
dp[0][0] = 0
dirr = [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)]

queue = [(0, start[0], start[1], 0)]

while queue:
    ind, y, x, direc = heapq.heappop(queue)

    if ind == n:
        break

    for t in range(5):
        dy = dirr[t][0]
        dx = dirr[t][1]
        if 0 <= lis[ind][0] + dy <= 100000 and 0 <= lis[ind][1] + dx <= 100000 and dp[ind][direc] + abs(y - lis[ind][0] - dy) + abs(x - lis[ind][1] - dx) < dp[ind+1][t]:
            dp[ind+1][t] = dp[ind][direc] + abs(y - lis[ind][0] - dy) + abs(x - lis[ind][1] - dx)
            heapq.heappush(queue, (ind+1, lis[ind][0] + dy, lis[ind][1] + dx, t))

print(min(dp[-1]))
