def solution(m, n, puddles):
    field = [[0] * (m+1) for _ in range(n+1)]

    for x,y in puddles:
        field[y][x] = -1
    field[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if field[i][j] == -1:
                field[i][j] = 0
            elif i == 1 and j == 1:
                pass
            else:    
                field[i][j] = (field[i-1][j] + field[i][j-1])
    
    
    return field[-1][-1] % 1000000007