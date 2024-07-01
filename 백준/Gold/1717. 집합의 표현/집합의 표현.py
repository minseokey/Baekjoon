import sys

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

uf = [i for i in range(n + 1)]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        uf[a] = b
    elif a < b:
        uf[b] = a


def find(a):
    if a == uf[a]:
        return a
    uf[a] = find(uf[a])
    return uf[a]


for _ in range(m):
    o, a, b = map(int, sys.stdin.readline().split())
    if o == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)