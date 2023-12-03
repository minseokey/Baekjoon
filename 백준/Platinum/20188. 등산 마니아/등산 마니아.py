import sys
sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
v = [[] for _ in range(N+1)]
d = [0] * (N+1)
ans = 0
NN = N * (N - 1) // 2
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    v[a].append(b)
    v[b].append(a)


def dfs(cur, pre):
    global ans
    d[cur] = 1
    for i in v[cur]:
        if i != pre:
            d[cur] += dfs(i, cur)
    ans += NN - ((N - d[cur]) * (N - d[cur] - 1) // 2)
    return d[cur]


dfs(1,0)
print(ans - NN)
