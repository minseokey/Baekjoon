import sys
import heapq
n = int(sys.stdin.readline())
maxHeap = []
for i in range(n):
    input = int(sys.stdin.readline())
    if len(maxHeap) == 0 and input == 0:
        print(0)
    elif input == 0:
        print(heapq.heappop(maxHeap)[1])
    else:
        heapq.heappush(maxHeap,(-input,input))