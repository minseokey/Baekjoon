from collections import defaultdict

def solution(n, results):
    dic_win = defaultdict(set)
    dic_lose = defaultdict(set)
    for _ in range(n):
        for win, lose in results:
            dic_win[win].add(lose)
            dic_win[win] = dic_win[win].union(dic_win[lose])
            dic_lose[lose].add(win)
            dic_lose[lose] = dic_lose[lose].union(dic_lose[win])
    
    ans = 0
    for i in range(1,n+1):
        if len(dic_win[i]) + len(dic_lose[i]) == n-1:
            ans += 1
    
    return ans