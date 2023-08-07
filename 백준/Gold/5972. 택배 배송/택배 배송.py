import heapq
import sys

n, m = map(int, sys.stdin.readline().split())

dic = dict()
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    if a in dic.keys():
        dic[a].append([c, b])
    else:
        dic[a] = [[c, b]]

    if b in dic.keys():
        dic[b].append([c, a])
    else:
        dic[b] = [[c, a]]

start = 0
heapqueue = [(0,0)]
dist = [float('inf')] * n
dist[0] = 0


while heapqueue:
    temp = heapq.heappop(heapqueue)
    for i in dic[temp[1]]:
        if dist[i[1]] > temp[0] + i[0]:
            dist[i[1]] = temp[0] + i[0]
            heapq.heappush(heapqueue,(temp[0]+i[0], i[1]))


print(dist[n-1])