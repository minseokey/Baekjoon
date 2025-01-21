from collections import defaultdict
import heapq

def solution(n, costs):
    dic = defaultdict(list)
    for i in costs:
        dic[i[0]].append([i[1],i[2]])
        dic[i[1]].append([i[0],i[2]])
    # 프림을 통해 알아보자.
    
    queue = [(0,0)] # 0 번째 시작점.
    visited = [False for _ in range(n)]
    wei = 0
    
    while queue:
        now_wei, now_node = heapq.heappop(queue)
        if visited[now_node] == False:
            visited[now_node] = True
            wei += now_wei
        
            for nex_node, nex_wei in dic[now_node]:
                if visited[nex_node] == False:
                    heapq.heappush(queue, (nex_wei, nex_node))
    
    return wei
    
    
    