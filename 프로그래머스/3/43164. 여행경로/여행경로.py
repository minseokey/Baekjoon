from collections import defaultdict
import heapq

def solution(tickets):
    tic = defaultdict(list)
    
    for s,e in tickets:
        tic[s].append(e)
    
    routes = ["ICN"]
    ans = []
    
    def recur():
        nonlocal ans
        
        if len(routes) == len(tickets) + 1:
            ans.append(routes.copy())

        for i in range(len(tic[routes[-1]])):
            now = tic[routes[-1]].pop(i)
            routes.append(now)
            recur()
            routes.pop()
            tic[routes[-1]].insert(i,now)
        
        
    recur()
    
    
    return min(ans)