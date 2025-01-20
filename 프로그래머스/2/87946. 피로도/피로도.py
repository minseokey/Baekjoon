def solution(k, dungeons):
    
    ans = 0
    
    def recur(cnt, now_k):
        nonlocal ans
        ans = max(cnt, ans)
        for i in range(len(dungeons)):
            if now_k >= dungeons[i][0]:
                tmp = dungeons.pop(i)
                recur(cnt+1, now_k - tmp[1] )
                dungeons.insert(i,tmp)
    
    recur(0,k)
    
    return ans