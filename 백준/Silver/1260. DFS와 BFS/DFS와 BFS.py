import sys
from collections import defaultdict, deque

n,m,v = map(int,sys.stdin.readline().split())

# 처음에 길 그래프 만들기
road = defaultdict(list)
for i in range(m):
    s,e = map(int, sys.stdin.readline().split())
    road[s].append(e)
    road[e].append(s)

# 각각의 연결가능한 지점 정렬하기
for i in range(1, n + 1):
    if i in road.keys():
        road[i].sort()

# 이미 방문한 노드 처리하기
v_dfs = [False] * (n+1)
v_bfs = [False] * (n+1)

# dfs
d_queue = deque([v])
d_ans = []

while d_queue:
    now = d_queue.pop()  # dfs
    
    # 방문처리
    if not v_dfs[now]:
        d_ans.append(now)
        v_dfs[now] = True

        if now in road.keys():
            # 다음 이동경로 -> 반대로 들어가야함
            for nex in road[now][::-1]:
                if not v_dfs[nex]:
                    d_queue.append(nex)


# bfs
b_queue = deque([v])
b_ans = []
while b_queue:
    now = b_queue.popleft()  # bfs
    
    # 방문처리
    if not v_bfs[now]:
        b_ans.append(now)
        v_bfs[now] = True
    
        # 다음 이동 경로
        if now in road.keys():
            for nex in road[now]:
                if not v_bfs[nex]:
                    b_queue.append(nex)

print(*d_ans)
print(*b_ans)