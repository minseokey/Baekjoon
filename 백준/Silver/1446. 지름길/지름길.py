import sys
from collections import deque

n, d = map(int, sys.stdin.readline().split())
dp = [i for i in range(10000)]
dp[0] = 0
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lis.sort()
lis = deque(lis)

for i in range(d + 1):
    if i == 0:
        dp[i] = min(1, dp[i])
    else:
        dp[i] = min(dp[i - 1] + 1, dp[i])

    while True:
        if lis and lis[0][0] == i:  # 지름길 시작점일때
            temp = lis.popleft()
            if temp[1] - temp[0] >= temp[2]:
                dp[temp[1]] = min(dp[i] + temp[2], dp[temp[1]])
        else:
            break


print(dp[d])
