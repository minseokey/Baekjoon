import sys

n = int(sys.stdin.readline())
for _ in range(n):
    length = int(sys.stdin.readline())
    lis = list(map(int, sys.stdin.readline().split()))

    dp = [[float('inf')] * (length) for _ in range(length)]
    addsum = [0]
    for i in range(length):
        dp[i][i] = 0
        addsum.append(addsum[-1] + lis[i])
    for i in range(1, length):  # 간격
        for j in range(length):  # 시작점
            if i + j < length:
                for k in range(j, j + i):  # 간격
                    dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + addsum[j + i + 1] - addsum[j])

    print(dp[0][-1])