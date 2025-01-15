import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    key = False
    cnt = 0
    while scoville:
        tmp = heapq.heappop(scoville)
        if tmp > K:
            key = True
            break
        if tmp < K and len(scoville) >= 1:
            nex = heapq.heappop(scoville)
            heapq.heappush(scoville, tmp + nex*2)
            cnt += 1
        elif len(scoville) == 0:
            break
            
    if key:
        return cnt
    else:
        return -1
    