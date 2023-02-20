def solution(m, n, puddles):
    lis = [[0 for i in range(m)]for j in range(n)]

    pudinx = m
    pudiny = n
    for i in range(n):
        for j in range(m):
            if [j+1,i+1] in puddles:
                lis[i][j] = float('inf')

                if j == 0:
                    pudiny = min(i,pudiny)
                if i == 0:
                    pudinx = min(j,pudinx)

    for i in range(pudiny):
        lis[i][0] = 1
    for i in range(pudinx):
        lis[0][i] = 1




    for i in range(1,n):
        for j in range(1,m):
            if lis[i][j] == float('inf'):
                pass
            else:
                if lis[i-1][j] == float('inf') or lis[i][j-1] == float('inf'):
                    lis[i][j] = min(lis[i-1][j],lis[i][j-1])
                else:
                    lis[i][j] = (lis[i-1][j] + lis[i][j-1])


    return lis[-1][-1]%1000000007