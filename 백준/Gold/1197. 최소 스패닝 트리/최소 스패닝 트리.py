import heapq
import sys
from collections import defaultdict

v, e = map(int, sys.stdin.readline().split())
field = defaultdict(list)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    field[a].append((b, c))
    field[b].append((a, c))

ans = 0
queue = [(0, 1)]
visited = [False] * (v+1)

while queue:
    w, now = heapq.heappop(queue)
    if not visited[now]:
        ans += w
        visited[now] = True
        for nex, nex_w in field[now]:
            heapq.heappush(queue, (nex_w, nex))

print(ans)
