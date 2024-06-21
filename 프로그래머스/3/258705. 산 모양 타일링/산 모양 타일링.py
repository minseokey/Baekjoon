def solution(n, tops):
    dp = [[0] * 4 for _ in range(n)]
    if tops[0] == 0:
        dp[0][0], dp[0][1], dp[0][2] = 1, 1, 1
    else:
        dp[0][0], dp[0][1], dp[0][2], dp[0][3] = 1, 1, 1, 1
        
    # 중앙 역삼각형의 소유를 어떤것이 하는가
    # 만약 이전 선택에서 2를 안했다 -> 
        # tops == 0: 중앙 소유는 0,1,2 가능
        # tops == 1: 중앙 소유는 0,1,2,3 가능.
    # 만약 이전 선택에서 2를 했다? -> 
        # tops == 0: 중앙소유는 0,2 
        # tops == 1: 중앙소유는 0,2,3
    
    for i in range(1, n):
        # 위에가 있으면
        if tops[i] == 1:
            for j in range(4):
                if j != 1:
                    dp[i][j] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3])%10007
                else:
                    dp[i][j] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3])%10007
        # 위에가 없으면
        else:
            for j in range(3):
                if j != 1:
                    dp[i][j] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3])%10007
                else:
                    dp[i][j] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3])%10007
    
    return sum(dp[-1])% 10007