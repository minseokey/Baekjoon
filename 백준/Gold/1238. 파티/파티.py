import copy
import heapq
import sys
from collections import deque

node, vertex, target = map(int, sys.stdin.readline().split())
dic = dict()
for i in range(vertex):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] not in dic.keys():
        dic[temp[0]] = [(temp[1], temp[2])]
    else:
        dic[temp[0]].append((temp[1], temp[2]))

#heapq사용, 거리를 앞으로, 노드는 뒤로)

def dijk(now, dijklis):
    queue = []
    heapq.heappush(queue,[0,now])

    while queue:
        temp = heapq.heappop(queue)
        for i in dic[temp[1]]:
            next_dis = dijklis[temp[1]] + i[1]
            if next_dis < dijklis[i[0]]:
                dijklis[i[0]] = next_dis
                heapq.heappush(queue,[next_dis,i[0]])

    return dijklis


dijkl1 = [float('inf') for a in range(node + 1)]
dijkl1[target] = 0
templis = dijk(target, dijkl1)

ansmax = 0
for i in range(1, node + 1):
    if i == target:
        pass
    else:
        # 가는길은 다익스트라로 각 노드에서 최소 거리를 찾아가는 방법으로
        dijkl = [float('inf') for a in range(node + 1)]
        dijkl[i] = 0
        ansmax = max(dijk(i, dijkl)[target]+templis[i],ansmax)

print(ansmax)












