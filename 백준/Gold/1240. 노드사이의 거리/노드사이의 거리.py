import sys

n, m = map(int, sys.stdin.readline().split())

node = {}
for i in range(n - 1):
    a, b, l = map(int, sys.stdin.readline().split())
    if a not in node.keys():
        node[a] = [(b, l)]
    else:
        node[a].append((b, l))
    if b not in node.keys():
        node[b] = [(a, l)]
    else:
        node[b].append((a, l))

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    visited = [False] * (n + 1)
    stack = [(start, 0)]
    key = False
    answer = 0
    while stack and not key:
        now, leng = stack.pop()
        visited[now] = True
        for next, nleng in node[now]:
            if next == end:
                key = True
                answer = leng + nleng
                break
            elif not visited[next]:
                stack.append((next, leng + nleng))
    print(answer)