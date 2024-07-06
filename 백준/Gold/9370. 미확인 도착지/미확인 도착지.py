import heapq
import sys
from collections import defaultdict

INF = int(1e9)

fois = int(sys.stdin.readline())
for _ in range(fois):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    path = defaultdict(list)
    road = -1
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        if road == -1 and (a, b) == (g, h) or (b, a) == (g, h):
            road = d
        path[a].append((b,d))
        path[b].append((a,d))

    endlis = [int(sys.stdin.readline()) for _ in range(t)]
    # s부터 출발, 반드시 g-h 길을 통과.

    def dijk(start):
        queue = [(start, 0)]
        dist = [INF] * (n + 1)
        dist[start] = 0
        while queue:
            now, weight = heapq.heappop(queue)
            if now in path.keys():
                for nex, nex_wei in path[now]:
                    if dist[now] + nex_wei < dist[nex]:
                        dist[nex] = dist[now] + nex_wei
                        heapq.heappush(queue, (nex, dist[nex]))

        return dist


    s_lis = dijk(s)
    g_lis = dijk(g)
    h_lis = dijk(h)

    anslis = []

    for e in endlis:
        if s_lis[h] + g_lis[e] + road == s_lis[e]:
            anslis.append(e)
        elif s_lis[g] + h_lis[e] + road == s_lis[e]:
            anslis.append(e)

    anslis.sort()
    print(*anslis)
