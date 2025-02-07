import heapq
import sys
from collections import defaultdict

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

field = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    field[a].append((b, c))


dist = [float('INF')] * (v + 1)
dist[k] = 0
queue = [(0, k)]

while queue:
    wei, now = heapq.heappop(queue)
    for nex, nex_w in field[now]:
        if dist[nex] > dist[now] + nex_w:
            dist[nex] = dist[now] + nex_w
            heapq.heappush(queue, (dist[nex], nex))

for i in range(1,len(dist)):
    if dist[i] == float('INF'):
        print("INF")
    else:
        print(dist[i])
