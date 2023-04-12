import heapq
import sys

city = int(sys.stdin.readline())
bus = int(sys.stdin.readline())
dic = {}
for i in range(bus):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] in dic.keys():
        dic[temp[0]].append((temp[1], temp[2]))
    else:
        dic[temp[0]] = [(temp[1], temp[2])]

start, end = map(int, sys.stdin.readline().split())

n = [int(1e9) for i in range(city + 1)]
queue = []
heapq.heappush(queue, (0, start))
n[start] = 0

while queue:
    wei, node = heapq.heappop(queue)
    if node in dic.keys() and dic[node]:
        while dic[node]:
            nexnode,nexweight = dic[node].pop()
            if wei + nexweight < n[nexnode]:
                n[nexnode] = wei + nexweight
                heapq.heappush(queue, (n[nexnode], nexnode))

print(n[end])
