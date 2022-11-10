import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
listCheck = [False] * n
graph = [[] for i in range(n)]
count = 0


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def Bfs(num):
    global count
    count += 1
    inputHeap = [num]
    listCheck[num] = True
    while inputHeap:
        target = heapq.heappop(inputHeap)
        for i in graph[target]:
            if not listCheck[i]:
                heapq.heappush(inputHeap, i)
                listCheck[i] = True


for i in range(n):
    if not listCheck[i]:
        Bfs(i)
print(count)