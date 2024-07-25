n = int(input())
if n == 0:
    print(0)
elif n == 2:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 1
    for i in range(4, n + 1, 2):
        temp = i-2
        for split in range(0, temp + 1, 2):
            dp[i] += (dp[split] * dp[temp-split]) % 987654321
    print(dp[-1] % 987654321)
