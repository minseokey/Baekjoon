import heapq
import sys

node,vertex = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
dic = dict()
for i in range(vertex):
    temp = list(map(int,sys.stdin.readline().split()))
    if temp[0] not in dic.keys():
        dic[temp[0]] = [[temp[1],temp[2]]]
    else:
        dic[temp[0]].append([temp[1],temp[2]])

def dijk(start,lis):
    q = []
    heapq.heappush(q,(0,start))
    lis[start] = 0
    while q:
        nowdist,nownode = heapq.heappop(q)
        if nownode in dic.keys():
            for i in dic[nownode]:
                newdist = i[1] + lis[nownode]
                if lis[i[0]] > newdist:
                    lis[i[0]] = newdist
                    heapq.heappush(q,(newdist,i[0]))

lis = [float('inf') for i in range(node+1)]
dijk(start,lis)

for i in range(1,len(lis)):
    if lis[i] == float('inf'):
        print("INF")
    else:
        print(lis[i])