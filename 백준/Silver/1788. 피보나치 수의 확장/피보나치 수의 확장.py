import sys

n = int(sys.stdin.readline())

is_m = False
if n < 0:
    is_m = True
    n = -n
if n == 0:
    print(0)
    print(0)
else:
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000

    if is_m and n % 2 == 0:
        print(-1)
    elif dp[-1] == 0:
        print(0)
    else:
        print(1)

    print(dp[-1])
