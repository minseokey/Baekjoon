import heapq
import itertools
import sys
from collections import deque

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while True:
    w, h = map(int, sys.stdin.readline().split())
    if h == w == 0:
        break
    else:
        field = []
        dust = []
        start = (-1, -1)
        for i in range(h):
            temp = list(sys.stdin.readline().strip())
            for j in range(w):
                if temp[j] == "o":
                    start = (i, j)
                if temp[j] == "*":
                    dust.append((i, j))
            field.append(temp)

    def route(start, end):
        queue = deque([(start[0], start[1], 0)])
        visited = [[False] * w for _ in range(h)]
        visited[start[0]][start[1]] = True
        while queue:
            ny, nx, c = queue.popleft()
            if (ny, nx) == end:
                return c
            for dy, dx in DIR:
                nny, nnx = ny + dy, nx + dx
                if 0 <= nny < h and 0 <= nnx < w and field[nny][nnx] != "x" and not visited[nny][nnx]:
                    queue.append((nny, nnx, c + 1))
                    visited[nny][nnx] = True
        return float('inf')

    dust_lis = [route(start, d) for d in dust]

    if any(d == float('inf') for d in dust_lis):
        print(-1)
        continue

    path = [[route(dust[i], dust[j]) for j in range(len(dust))] for i in range(len(dust))]

    queue = [(dust_lis[i], i, 1 << i) for i in range(len(dust))]
    heapq.heapify(queue)
    visited = {}

    while queue:
        cost, now, vis = heapq.heappop(queue)
        if vis == (1 << len(dust)) - 1:
            print(cost)
            break
        if (now, vis) in visited and visited[(now, vis)] <= cost:
            continue
        visited[(now, vis)] = cost
        for i in range(len(dust)):
            if not vis & (1 << i):
                heapq.heappush(queue, (cost + path[now][i], i, vis | (1 << i)))
    else:
        print(-1)
