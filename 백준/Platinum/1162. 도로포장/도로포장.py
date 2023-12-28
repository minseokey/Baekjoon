import heapq
import sys

n, m, k = map(int, sys.stdin.readline().split())
route = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    route[s].append((e, w))
    route[e].append((s, w))

distance = [[float("inf")] * (k + 1) for _ in range(n + 1)]
visited = [[False] * (k + 1) for _ in range(n + 1)]
queue = []
heapq.heappush(queue, (0, (1, 0)))
distance[1][0] = 0

while queue:
    dist, (temp, pave) = heapq.heappop(queue)

    if visited[temp][pave]:
        continue
    visited[temp][pave] = True

    for nex, weight in route[temp]:
        if pave < k and distance[nex][pave + 1] > dist:
            distance[nex][pave + 1] = dist
            heapq.heappush(queue, (distance[nex][pave + 1], (nex, pave + 1)))

        if distance[nex][pave] > dist + weight:
            distance[nex][pave] = dist + weight
            heapq.heappush(queue, (distance[nex][pave], (nex, pave)))

print(min(distance[n]))