import sys

n = int(sys.stdin.readline())
path = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    path[a].append(b)
    path[b].append(a)

# 가중합을 떠올릴수 있다.
# 리프부터 가는 최솟값을 모두 계산해보자.
short_path = [set() for _ in range(n + 1)]
visited = [False] * (n + 1)


def dfs(now, pathstack):
    short_path[now] = short_path[now].union(pathstack)
    for nex in path[now]:
        if not visited[nex]:
            visited[nex] = True
            pathstack.add(nex)
            dfs(nex, pathstack)
            pathstack.remove(nex)


visited[1] = True
dfs(1, {1})
count = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        count += len(short_path[i].union(short_path[j])) - 1
print(count)