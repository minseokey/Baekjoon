import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville:
        a = heapq.heappop(scoville)
        if a >= K:
            return count
        elif a<K and not scoville:
            return -1
        else:
            b = heapq.heappop(scoville)
            count += 1
            heapq.heappush(scoville,a+2*b)

    return -1



    