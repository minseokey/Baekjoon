import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline()) + 1

    dp = [[0] * target for _ in range(len(coin))]

    for i in range(coin[0], target, coin[0]):
        dp[0][i] = 1
    for i in range(len(coin)):
        dp[i][0] = 1

    for i in range(1, len(coin)):
        for j in range(target):
            if j >= coin[i]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coin[i]]
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[-1][-1])