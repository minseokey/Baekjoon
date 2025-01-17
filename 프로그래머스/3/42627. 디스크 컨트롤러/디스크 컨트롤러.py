import heapq
from collections import deque

def solution(jobs):
    # jobs -> 요청 시간, 작업 시간.
    jobs = deque(sorted(jobs))
    on_sche = []
    len_j = len(jobs)
    cnt = 0
    ans = 0
    
    while jobs or on_sche:
        # 타이밍 맞는 jobs 추가.
        while jobs:
            if cnt >= jobs[0][0]: 
                heapq.heappush(on_sche, tuple(reversed(jobs.popleft())))
            else:
                break

        # 가장 짧은 일 수행.
        if on_sche:
            tmp = heapq.heappop(on_sche)
            cnt += tmp[0]
            ans += cnt - tmp[1]
        else:
            cnt += 1
    
    return ans//len_j