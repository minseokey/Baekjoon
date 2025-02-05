import sys
from collections import defaultdict
import heapq

while True:
    home, path = map(int, sys.stdin.readline().split())
    if home == 0 and path == 0:
        break
    field = defaultdict(list)
    allpath = 0

    for _ in range(path):
        t = list(sys.stdin.readline().split())
        a, b, c = map(int, t)
        field[a].append((b, c))
        field[b].append((a, c))
        allpath += c


    queue = [(0, 0)]  # 가중치, 노드
    visited = [False] * home

    while queue:
        n_wei, n_node = heapq.heappop(queue)

        if not visited[n_node]:
            allpath -= n_wei
            visited[n_node] = True
            for nex_node, nex_wei in field[n_node]:
                if not visited[nex_node]:
                    heapq.heappush(queue, (nex_wei, nex_node))

    print(allpath)

