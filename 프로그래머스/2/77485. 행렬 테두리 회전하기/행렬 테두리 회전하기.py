def solution(rows, columns, queries):
    
    def spin(q):
        sy,sx,ey,ex = q
        
        # 그럼 범위는
        # x++ -> 여기서 남는거 temp 로 저장.
        # y++
        # x--
        # y-- -> 여기서 부족한거 temp로 넣기
        
        mi = float('inf')
        temp = field[sy][sx]
        # 1, sy
        for x in range(sx+1,ex+1):
            tt = field[sy][x]
            field[sy][x] = temp
            temp = tt
            mi = min(mi, field[sy][x])
            
            
        # 2, ex
        for y in range(sy+1,ey+1):
            tt = field[y][ex]
            field[y][ex] = temp
            temp = tt
            mi = min(mi, field[y][ex])
        
        # 3, ey
        for x in range(ex-1, sx-1,-1):
            tt = field[ey][x]
            field[ey][x] = temp
            temp = tt
            mi = min(mi, field[ey][x])
        
        # 4, sx
        for y in range(ey-1, sy-1 ,-1):
            tt = field[y][sx]
            field[y][sx] = temp
            temp = tt
            mi = min(mi, field[y][sx])
        
        return mi
        
        
        
    
    field = []
    k = 1
    for i in range(rows):
        temp = [tempk for tempk in range(k,k+columns)]
        field.append(temp)
        k += columns
    
    ans = []
    for i in queries:
        for j in range(4):
            i[j] -= 1
        ans.append(spin(i))
    
    return ans
    
    