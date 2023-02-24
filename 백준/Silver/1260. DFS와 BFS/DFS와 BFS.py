import sys
from collections import deque

vertex = dict()
n,m,v = map(int,sys.stdin.readline().split())
for i in range(m):
    tempa,tempb = map(int,sys.stdin.readline().split())
    if tempa in vertex.keys():
        vertex[tempa].append(tempb)
    else:
        vertex[tempa] = [tempb]
    if tempb in vertex.keys():
        vertex[tempb].append(tempa)
    else:
        vertex[tempb] = [tempa]


checkdfs = [False for i in range(n)]
dfsans = []

def dfs(check, now):
    dfsans.append(now)
    check[now-1] = True
    if now in vertex.keys():
        for i in sorted(vertex[now]):
            if not check[i-1]:
                dfs(check,i)
    else:
        return


dfs(checkdfs,v)
print(*dfsans)

queue = deque()
queue.append(v)
bfsans = []
checkbfs = [False for i in range(n)]
while queue:
    temp = queue.popleft()
    if not checkbfs[temp - 1]:
        bfsans.append(temp)
    checkbfs[temp - 1] = True
    if temp in vertex.keys():
        for i in sorted(vertex[temp]):
            if not checkbfs[i - 1]:
                queue.append(i)

print(*bfsans)