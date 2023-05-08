i = int(input())

lis = [0 for k in range(10 ** 6 + 1)]
dp = [str(k) for k in range(10 ** 6 + 1)]

for n in range(2,10 ** 6 + 1):
    if n % 6 == 0:
        # -1
        if min(lis[n // 3], lis[n // 2], lis[n - 1]) == lis[n - 1]:
            lis[n] = lis[n - 1] + 1
            dp[n] = dp[n] + " " + dp[n - 1]

        # //2
        elif min(lis[n // 3], lis[n // 2], lis[n - 1]) == lis[n // 2]:
            lis[n] = lis[n // 2] + 1
            dp[n] = dp[n] + " " + dp[n // 2]

        # //3
        elif min(lis[n // 3], lis[n // 2], lis[n - 1]) == lis[n // 3]:
            lis[n] = lis[n // 3] + 1
            dp[n] = dp[n] + " " + dp[n // 3]

    elif n % 3 == 0:
        # -1
        if min(lis[n // 3], lis[n - 1]) == lis[n - 1]:
            lis[n] = lis[n - 1] + 1
            dp[n] = dp[n] + " " + dp[n - 1]

        # //3
        else:
            lis[n] = lis[n // 3] + 1
            dp[n] = dp[n] + " " + dp[n // 3]

    elif n % 2 == 0:
        # -1
        if min(lis[n // 2], lis[n - 1]) == lis[n - 1]:
            lis[n] = lis[n - 1] + 1
            dp[n] = dp[n] + " " + dp[n - 1]

        # //2
        else:
            lis[n] = lis[n // 2] + 1
            dp[n] = dp[n] + " " + dp[n // 2]

    else:
        # -1
        if n >= 1:
            lis[n] = lis[n - 1] + 1
            dp[n] = dp[n] + " " + dp[n - 1]

print(lis[i])
print(dp[i])

