import sys
import heapq
n = int(sys.stdin.readline())
leastHeap = []
for i in range(n):
    input = int(sys.stdin.readline())
    if len(leastHeap) == 0 and input == 0:
        print(0)
    elif input == 0:
        print(heapq.heappop(leastHeap))
    else:
        heapq.heappush(leastHeap,input)