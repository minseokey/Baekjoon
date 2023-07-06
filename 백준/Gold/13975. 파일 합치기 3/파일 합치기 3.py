import copy
import heapq
import sys

fois = int(input())
for _ in range(fois):
    n = int(input())
    lis = list(map(int,sys.stdin.readline().split()))

    heapq.heapify(lis)
    ans = 0
    while len(lis) > 1:
        a = heapq.heappop(lis)
        b = heapq.heappop(lis)
        ans += a+b
        heapq.heappush(lis,a+b)

    print(ans)