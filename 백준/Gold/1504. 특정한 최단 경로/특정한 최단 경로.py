import heapq
import sys

node, vertex = map(int, sys.stdin.readline().split())

dic = dict()
for i in range(vertex):
    a, b, weight = map(int, sys.stdin.readline().split())

    if a not in dic.keys():
        dic[a] = [(b, weight)]
    else:
        dic[a].append((b, weight))
    if b not in dic.keys():
        dic[b] = [(a, weight)]
    else:
        dic[b].append((a, weight))

roada, roadb = map(int, sys.stdin.readline().split())


# 다익스트라 진행, 힙큐 다익스트라
# 다익스트라 함수를 만들어서 (1->v1 + v1->v2 + v2->node), (1->v2 + v2->v1 + v1->node) 를 계산, 더 작은놈을 파악하자.

def dijk(start, end):
    dijklis = [float('inf') for k in range(node + 1)]
    dijklis[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    dijklis[start] = 0

    while q:
        distnow, now = heapq.heappop(q)
        if now in dic.keys():
            for new, distnew in dic[now]:
                if dijklis[new] > distnew + distnow:
                    dijklis[new] = distnew + distnow
                    heapq.heappush(q, (distnew + distnow, new))

    return dijklis[end]


right = dijk(1, roada) + dijk(roada, roadb) + dijk(roadb, node)
left = dijk(1, roadb) + dijk(roadb, roada) + dijk(roada, node)
if right == float('inf') and left == float('inf'):
    print(-1)
else:
    print(min(right, left))