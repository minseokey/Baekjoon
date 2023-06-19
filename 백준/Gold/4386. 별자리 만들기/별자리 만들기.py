import copy
import math
import sys

n = int(sys.stdin.readline())
lis = [list(map(float, sys.stdin.readline().split())) for i in range(n)]
dis = []
uf = [i for i in range(n + 1)]
for i in range(len(lis)):
    for j in range(i + 1, len(lis)):
        di = round(math.sqrt((lis[i][0] - lis[j][0]) ** 2 + (lis[i][1] - lis[j][1]) ** 2), 5)
        dis.append([di, i, j])

visit = [False for i in range(n)]
dis.sort()

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

ans = 0
while dis:
    tp = dis.pop(0)
    if find(tp[2]) != find(tp[1]):
        union(tp[2],tp[1])
        ans += tp[0]

print(round(ans, 2))
