from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while True:
        ans = 0
        for ind in range(len(speeds)):
            progresses[ind] += speeds[ind]
        
        while progresses:
            if progresses[0] >= 100:
                ans += 1
                progresses.popleft()
                speeds.popleft()
            else:
                break
                
        if ans > 0:
            answer.append(ans)
        
        if not progresses:
            break
            
    return answer