def solution(routes):
    routes.sort()
    
    ans = 1
    now_start = routes[0][0]
    now_end = routes[0][1]
    
    for i in routes:   
        if i[0] > now_end:
            now_start = i[0]
            now_end = i[1]
            ans += 1
        elif now_end > i[1]:
            now_end = i[1]
        
        print(now_start, now_end)
    
    
        
    return ans