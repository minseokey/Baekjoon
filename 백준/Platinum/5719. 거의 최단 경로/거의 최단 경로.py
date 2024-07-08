import heapq
import sys
from collections import defaultdict, deque

INF = float('inf')

while True:
    n, m = map(int, sys.stdin.readline().split())
    if (n, m) == (0, 0):
        break
    else:
        s, d = map(int, sys.stdin.readline().split())
        path = defaultdict(set)
        path_reverse = defaultdict(set)
        path_checked = [[False] * n for _ in range(n)]
        for i in range(m):
            st, en, w = map(int, sys.stdin.readline().split())
            path[st].add((en, w))
            path_reverse[en].add((st, w))


    # 첫번쨰 다익스트라는 그냥 계산
    def dijk():
        vis = [INF] * n
        vis[s] = 0
        queue = [(0, s)]
        while queue:
            now_wei, now = heapq.heappop(queue)
            if now in path.keys():
                for nex, nex_wei in path[now]:
                    if vis[nex] > now_wei + nex_wei and not path_checked[now][nex]:
                        vis[nex] = now_wei + nex_wei
                        heapq.heappush(queue, (vis[nex], nex))
        return vis


    # 최단거리 추가
    first = dijk()
    shortest = first[d]
    if shortest == INF:
        print(-1)
        continue

    # BFS 를 통한 최단 경로 저장, 여기에 들어가는 경로를 check 로 바꿔주자.
    queue = deque([(0, d)]) # 뒤로부터 더해가자 with path_reverse
    while queue:
        now_wei, now = queue.popleft()
        for prev, prev_wei in path_reverse[now]:
            if now_wei + prev_wei + first[prev] == shortest and not path_checked[prev][now]: # 끝 - now, now - nex, nex - 최단거리 == shortest
                queue.append((now_wei + prev_wei, prev))
                path_checked[prev][now] = True


    ans = dijk()
    if ans[d] == INF:
        print(-1)
    else:
        print(ans[d])
