import itertools
import sys
from collections import deque


def bfs(lis):
    if not lis:
        return 0, 0
    nodenum = 0
    summ = 0
    start = lis[0]
    queue = deque([start])
    visited = {start}
    while queue:
        temp = queue.pop()
        nodenum += 1
        summ += ppt[temp]
        if temp in linkdict.keys():
            for k in linkdict[temp]:
                if k not in visited and k in lis:
                    visited.add(k)
                    queue.append(k)
    return summ, nodenum

def gary(lis):
    global ans
    alis = lis
    blis = [k for k in range(n) if k not in lis]
    sum_a, node_a = bfs(alis)
    sum_b, node_b = bfs(blis)
    if node_a + node_b == n:
        ans = min(ans, abs(sum_a - sum_b))


n = int(sys.stdin.readline())
ppt = list(map(int, sys.stdin.readline().split()))
linkdict = {}
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in temp[1:]:
        if i not in linkdict.keys():
            linkdict[i] = [j-1]
        else:
            linkdict[i].append(j-1)

# 두개로 나누기
pptlis = [i for i in range(n)]
splitlis = []
for i in range(1, n // 2 + 1):
    splitlis += list(itertools.combinations(pptlis, i))

ans = float('inf')
for i in splitlis:
    gary(list(i))

if ans == float('inf'):
    print(-1)
else:
    print(ans)