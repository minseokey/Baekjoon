import bisect
import sys
from collections import deque

n = int(sys.stdin.readline())
lis = []
for i in range(n):
    lis.append(int(sys.stdin.readline()))

# 그냥 가장 긴 증가하는 부분 순열 만들고, 거기서 빼주면 될듯. -> n - lis

dp = []

for i in lis:
    temp = bisect.bisect_left(dp, i)
    if temp == len(dp):
        dp.append(i)
    else:
        dp[temp] = i

print(n - len(dp))