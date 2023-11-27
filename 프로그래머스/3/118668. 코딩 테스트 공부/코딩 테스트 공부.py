def solution(alp, cop, problems):
    # 일단 변수가 두개네? 2차 dp
    # 일단 모든 문제를 풀 수 있다 -> 가장 높은 alp, cop 만족.
    maxalp = alp
    maxcop = cop
    for i in problems:
        if i[0] > maxalp:
            maxalp = i[0]
        if i[1] > maxcop:
            maxcop = i[1]

    if maxalp <= alp:
        alp = maxalp
    if maxcop <= cop:
        cop = maxcop

    # x축 alp, y축 cop 안의 값 -> 드는 시간
    dp = [[float('inf')] * (maxcop * 2) for _ in range(maxalp * 2)]
    # 원래 가지고 있는 alp, cop 까지 모두 0 만들기
    dp[alp][cop] = 0

    # 이제 dp 시작
    for i in range(alp, maxalp + 1):
        for j in range(cop, maxcop + 1):
            if i+1 <= maxalp:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            if j+1 <= maxcop:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            for pr in problems:
                if i >= pr[0] and j >= pr[1]:
                    dp[min(i + pr[2],maxalp)][min(j + pr[3],maxcop)] = min(dp[i][j] + pr[4], dp[min(i + pr[2],maxalp)][min(j + pr[3],maxcop)])

    tempans = dp[maxalp][maxcop]
    return tempans