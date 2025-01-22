from collections import deque

def solution(begin, target, words):
    
    def is_sim(a,b):
        cnt = 1
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt -= 1
        if cnt == 0:
            return True
        return False
    
    queue = deque([(begin, 0)])
    visited = dict()
    ans = float("INF")
    for i in words:
        visited[i] = False
    
    while queue:
        now, cnt = queue.popleft()
        if now == target:
            ans = min(ans, cnt)
            continue
        
        for i in words:
            if is_sim(now, i) and visited[i] == False:
                queue.append((i, cnt + 1))
                visited[i] = True
    
    if ans == float("INF"):
        return 0
    return ans