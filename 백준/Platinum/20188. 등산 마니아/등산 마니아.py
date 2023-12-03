import sys


def dfs(cur):
    global ans
    d[cur] = 1
    for i in v[cur]:
        if not d[i]:
            d[cur] += dfs(i)
    ans += ret(N) - ret(N - d[cur])
    return d[cur]

def ret(n):
    return n * (n - 1) // 2

N = int(sys.stdin.readline())
v = [[] for _ in range(N + 1)]
d = [0] * (N + 1)
ans = 0

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    v[a].append(b)
    v[b].append(a)

dfs(1)
print(ans - ret(N))