import heapq
import sys

n = int(sys.stdin.readline().replace("\n", ""))
head = int(sys.stdin.readline().replace("\n", ""))

bigheap = []
smallheap = []
heapq.heappush(bigheap, head)
print(head)
for i in range(n - 1):
    now = int(sys.stdin.readline().replace("\n", ""))


    if now < head:
        heapq.heappush(smallheap, -now)
    else:
        heapq.heappush(bigheap, now)

    if len(bigheap) - len(smallheap) > 1:
        heapq.heappush(smallheap, -heapq.heappop(bigheap))
    elif len(smallheap) - len(bigheap) > 1:
        heapq.heappush(bigheap, -heapq.heappop(smallheap))




    # 홀수
    if len(smallheap) > len(bigheap):
        head = -heapq.heappop(smallheap)
        print(head)
        heapq.heappush(smallheap, -head)

    elif len(bigheap) > len(smallheap):
        head = heapq.heappop(bigheap)
        print(head)
        heapq.heappush(bigheap, head)

    # 짝수
    else:
        headsmall = -heapq.heappop(smallheap)
        headbig = heapq.heappop(bigheap)

        if headsmall > headbig:
            print(headbig)
        else:
            print(headsmall)

        head = (headbig + headsmall)/2
        heapq.heappush(bigheap, headbig)
        heapq.heappush(smallheap, -headsmall)