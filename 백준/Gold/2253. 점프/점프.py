import heapq
import sys

n, m = map(int, sys.stdin.readline().split())

lis = [True] * (n + 1)
for i in range(m):
    lis[int(sys.stdin.readline())] = False

dp = [float("inf")] * (n + 1)
dp[1] = 0

queue = [(0, 1, 1)]
dic = dict()
key = False
while queue:
    count, now, jump = heapq.heappop(queue)
    if now == n:
        print(count)
        key = True
        break
    if 0 < now + jump <= n and 0 < jump and lis[now + jump] and (
            (now, jump) not in dic.keys() or dic[(now, jump)] > count):
        heapq.heappush(queue, (count + 1, now + jump, jump + 1))
        heapq.heappush(queue, (count + 1, now + jump, jump))
        heapq.heappush(queue, (count + 1, now + jump, jump - 1))
        dp[now + jump] = min(dp[now + jump], dp[now] + 1)
        dic[(now, jump)] = count

if not key:
    print(-1)
