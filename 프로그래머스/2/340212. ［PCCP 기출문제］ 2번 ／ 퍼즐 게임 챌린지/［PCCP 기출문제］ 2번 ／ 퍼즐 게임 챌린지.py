def solution(diffs, times, limit):
    
    # 계산식 산출
    def calc(level):
        ans = times[0]
        for i in range(1, len(diffs)):
            time_cur = times[i]
            time_prev = times[i-1]
            diff = diffs[i]
            if diff <= level:
                ans += time_cur
            else:
                ans += (diff-level) * (time_cur+time_prev) + time_cur 
        return ans
    
    # 이분탐색
    start = 1
    end = max(diffs)
    mid = -1
    answer = 0
    while start <= end:

        mid = (start+end) // 2
        midcalc = calc(mid)
        
        if midcalc > limit:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    
    return answer
