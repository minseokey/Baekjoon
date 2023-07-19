n = int(input())

dp = [0 for _ in range(n)]
if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = (dp[i-2]+(dp[i-1]*2))% 9901


    print((sum(dp) * 2 + 1)%9901)