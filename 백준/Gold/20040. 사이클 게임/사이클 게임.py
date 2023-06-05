import sys

n,m = map(int,sys.stdin.readline().split())


uf = [i for i in range(n)]

def find(v):
    if v == uf[v]:
        return uf[v]
    return find(uf[v])

def union(a,b):
    fa = find(a)
    fb = find(b)
    if fa == fb:
        return True
    elif fa > fb:
        uf[fa] = fb
    else:
        uf[fb] = fa

temp = 0
key = False
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if union(a,b):
        temp = i+1
        key = True
        break

if not key:
    print(0)
else:
    print(temp)