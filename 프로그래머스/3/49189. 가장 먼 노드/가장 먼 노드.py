from collections import Counter,defaultdict
import heapq

def solution(n, edge):
    # 다익스트라 타서 가장 작은 거리 찾으면 되는거 아냐?
    dic = defaultdict(list)
    for a,b in edge:
        dic[a].append(b)
        dic[b].append(a)
    
    queue = [(0,1)]
    distance = [float("INF")] * (n+1)
    distance[0] = 0
    distance[1] = 0
    
    while queue:
        n_wei, n_node = heapq.heappop(queue)
        
        for nex_node in dic[n_node]:
            if distance[nex_node] > distance[n_node] + 1:
                distance[nex_node] = distance[n_node] + 1
                heapq.heappush(queue, (distance[nex_node], nex_node))

    ans = 0
    for i in distance:
        if i == max(distance):
            ans += 1
    
    return ans