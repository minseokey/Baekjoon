import heapq
import sys

n = int(sys.stdin.readline())
queue = []
lis = []
for i in range(n):
    dead, ramen = map(int,sys.stdin.readline().split())
    lis.append((dead,ramen))

lis.sort()

ans = 0
for i in range(n,0,-1):
    # dead 가 i 보다 작고 값이 최대인것 합.
    while lis:
        td, tm = lis.pop()
        if td >= i:
            heapq.heappush(queue, (-tm, td))

        else:
            lis.append((td,tm))
            break

    while queue:
        tm, td = heapq.heappop(queue)
        if td >= i:
            ans -= tm
            break


print(ans)