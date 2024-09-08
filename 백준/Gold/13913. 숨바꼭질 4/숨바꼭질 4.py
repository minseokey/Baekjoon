import heapq
import sys

n, k = map(int, sys.stdin.readline().split())

# Case -> x-1, x+1, 2x

visited = [-1] * ((max(k, n) * 2)+1)
queue = [(0, n, -3)]
ans = 0
while queue:
    cnt, place, bef = heapq.heappop(queue)
    if visited[place] == -1:
        visited[place] = bef
        if place == k:
            ans = cnt
            break
        if place >= 1:
            heapq.heappush(queue, (cnt + 1, place - 1, place))
        if place < k * 2:
            heapq.heappush(queue, (cnt + 1, place + 1, place))
        if place < k:
            heapq.heappush(queue, (cnt + 1, place * 2, place))

lis = []
temp = k
while temp != -3:
    lis.append(temp)
    temp = visited[temp]
lis.reverse()

print(ans)
print(*lis)