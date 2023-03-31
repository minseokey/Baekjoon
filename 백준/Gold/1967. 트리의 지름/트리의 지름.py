import sys
from collections import deque

n = int(sys.stdin.readline())
nodedict = dict()
nodealldict = dict()
for i in range(n-1):
    par,off,wei = map(int,sys.stdin.readline().split())
    if par not in nodedict.keys():
        nodedict[par] = [[off,wei]]
    else:
        nodedict[par].append([off,wei])
    if par not in nodealldict.keys():
        nodealldict[par] = [[off, wei]]
    else:
        nodealldict[par].append([off, wei])
    if off not in nodealldict.keys():
        nodealldict[off] = [[par, wei]]
    else:
        nodealldict[off].append([par, wei])

# 1. 루트에서 가장 먼 노드를 찾아가자.
maxx = [0,0]
queue = deque()
queue.append([1,0])
while queue:
    tempnode, tempwei = queue.popleft()
    if tempnode not in nodedict.keys():
        if maxx[1] < tempwei:
            maxx = [tempnode,tempwei]
    else:
        for i in nodedict[tempnode]:
            queue.append([i[0],i[1] + tempwei])


# 2. 아까찾은 노드에서 가장 먼 노드를 찾아가자.

maxx1 = [maxx[0],0]
queue1 = deque()
queue1.append(maxx1)
visitednode = [False for a in range(n + 1)]
visitednode[maxx[0]] = True
while queue1:
    tempnode, tempwei = queue1.popleft()
    if maxx1[1] < tempwei:
        maxx1 = [tempnode, tempwei]
    if tempnode in nodealldict.keys():
        for i in nodealldict[tempnode]:
            if not visitednode[i[0]]:
                visitednode[i[0]] = True
                queue1.append([i[0], i[1] + tempwei])

print(maxx1[1])