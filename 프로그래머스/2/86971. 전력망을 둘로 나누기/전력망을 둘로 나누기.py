from collections import Counter

def solution(n, wires):
    
    def cut(exp):
        uf = [i for i in range(n + 1)]
        
        def find(a):
            if a != uf[a]:
                uf[a] = find(uf[a])
            return uf[a]

        def union(a,b):
            a = find(a)
            b = find(b)
            if a > b:
                uf[a] = b
            else:
                uf[b] = a
        
        for i in range(len(wires)):
            if exp != i:
                union(wires[i][0], wires[i][1])
        
        uf = [find(i) for i in range(1, n+1)]
        
        tmp = list(dict(Counter(uf)).values())
        return abs(tmp[1] - tmp[0])
        
        
    ans = float("INF")
    for i in range(len(wires)):
        ans = min(ans, cut(i))
    
    return ans