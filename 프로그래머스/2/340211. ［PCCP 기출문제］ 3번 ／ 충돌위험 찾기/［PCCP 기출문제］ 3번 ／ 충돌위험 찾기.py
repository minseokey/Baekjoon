from collections import Counter

def solution(points, routes):
    ans = 0
    all_routes = []
    for i in range(len(routes)):
        tmp = [tuple(points[routes[i][0]-1])]
        s_y,s_x = 0,0
        for j in range(len(routes[i])-1):
            s_y, s_x = points[routes[i][j] - 1]
            e_y, e_x = points[routes[i][j+1] - 1]
            
            # y이동
            while s_y != e_y:
                if s_y > e_y:
                    s_y -= 1
                elif s_y < e_y:
                    s_y += 1
                tmp.append((s_y, s_x))
            # x이동
            while s_x != e_x:
                if s_x > e_x:
                    s_x -= 1
                elif s_x < e_x:
                    s_x += 1
                tmp.append((s_y, s_x))
        
        all_routes.append(tmp)
    
    for i in range(len(max(all_routes, key = lambda x:len(x)))):
        tmp = []
        for j in range(len(all_routes)):
            if len(all_routes[j]) > i:
                tmp.append(all_routes[j][i])
        
        for i in Counter(tmp).values():
            if i != 1:
                ans += 1
        
    return ans
    
    
    
    
    
    