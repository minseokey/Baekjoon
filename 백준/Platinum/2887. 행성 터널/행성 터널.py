import copy
import sys

n = int(sys.stdin.readline())
lis = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
uf = [i for i in range(n)]

for i in range(n):
    lis[i].append(i)


def find(a):
    if a == uf[a]:
        return a
    return find(uf[a])


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    elif a > b:
        uf[a] = b
        return True
    else:
        uf[b] = a
        return True


# 거리가 작은 순으로 나열.
distan = set()
lis0 = copy.deepcopy(lis)
lis1 = copy.deepcopy(lis)
lis2 = copy.deepcopy(lis)
lis0.sort(key=lambda x: x[0])
lis1.sort(key=lambda x: x[1])
lis2.sort(key=lambda x: x[2])

for i in range(1, n):
    dis0 = (lis0[i][3],lis0[i-1][3],min(abs(lis0[i][0] - lis0[i - 1][0]), abs(lis0[i][1] - lis0[i - 1][1]), abs(lis0[i][2] - lis0[i-1][2])))
    dis1 = (lis1[i][3],lis1[i-1][3],min(abs(lis1[i][0] - lis1[i - 1][0]), abs(lis1[i][1] - lis1[i - 1][1]), abs(lis1[i][2] - lis1[i-1][2])))
    dis2 = (lis2[i][3],lis2[i-1][3],min(abs(lis2[i][0] - lis2[i - 1][0]), abs(lis2[i][1] - lis2[i - 1][1]), abs(lis2[i][2] - lis2[i-1][2])))
    distan.add(dis0)
    distan.add(dis1)
    distan.add(dis2)

distan = list(distan)
distan.sort(key=lambda x: x[2])
visited = [2 for i in range(n)]
ans = 0

# 크루스칼 만들기
for i in distan:
    ts, te, wei = i
    if find(ts) != find(te):
        union(ts,te)
        ans += wei

print(ans)
