import sys

n, m = map(int,sys.stdin.readline().split())
path = []
for i in range(m):
    path.append(tuple(map(int,sys.stdin.readline().split())))


# belman-ford
dist = [float('inf')] * (n+1)


dist[1] = 0
# 매 노드마다 하나의 라운드. 일반적인 간선은 node - 1 개일때 최솟값이 나오고 끝이 나야함.
# 근데 만약 한번 더 진행할때도 줄어든다? -> 음의 사이클 검출이다.
for i in range(n-1): #
    # 매 라운드마다 모든간선 체크
    for s,e,w in path:
        if dist[e] > dist[s] + w:
            dist[e] = dist[s] + w

is_cycle = False
# 한번더 진행 후 테스트
for s,e,w in path:
    if dist[e] > dist[s] + w:
        is_cycle = True
        break

if is_cycle:
    print(-1)
else:
    for i in range(2, len(dist)):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])