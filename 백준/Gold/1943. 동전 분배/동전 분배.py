import copy
import sys

for i in range(3):
    n = int(sys.stdin.readline())
    lis = []
    sum = 0
    key = True
    for j in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if key and b % 2 == 1:
            key = False
        lis += [a] * b
        sum += (a * b)

    if key == True:
        print(1)
    elif sum % 2 != 0:
        print(0)
    else:
        target = sum // 2
        lis.sort(reverse=True)
        dp = [0 for _ in range(target + 1)]

        for j in lis:
            for k in range(target - j, -1, -1):
                if dp[k + j] < dp[k] + j:
                    dp[k + j] = dp[k] + j

        if dp[-1] == target:
            print(1)
        else:
            print(0)
