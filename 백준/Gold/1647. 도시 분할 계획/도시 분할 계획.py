import heapq
import sys
n,m = map(int,sys.stdin.readline().split())

def find(a):
    if a == uf[a]:
        return a
    return find(uf[a])

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        uf[a] = b
    else:
        uf[b] = a

lis= []
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    lis.append([a,b,c])

lis.sort(key=lambda x:x[2])
uf = [i for i in range(n)]
weight = []


for ta,tb,w in lis:
    if find(ta-1) != find(tb-1):
        weight.append(w)
        union(ta-1,tb-1)


print(sum(weight) - max(weight))




