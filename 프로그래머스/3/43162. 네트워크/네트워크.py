from collections import defaultdict

def solution(n, computers):
    route = defaultdict(set)
    for i in range(n):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                route[i].add(j)
                route[j].add(i)
                   
    uf = [i for i in range(n)]
    
    def find(a):
        if uf[a] != a:  
            uf[a] = find(uf[a])
        return uf[a] 
    
    def union(a,b):
        a = find(a) 
        b = find(b)
        
        if a > b:
            uf[a] = b
        elif b > a:
            uf[b] = a
    
    for i in route.keys():
        for j in route[i]:
            union(i,j)
    
    return len(set(uf))
    
    
    