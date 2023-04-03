# 도가뉴의 항등식
# a(2n) => a(n) [a(n) + 2a(n-1)]
# a(2n + 1) => a(n)**2 + a(n-1)**2
import sys

n = int(sys.stdin.readline())

dp = dict()
dp[0] = 0
dp[1] = 1
dp[2] = 1

def recur(n):
    if n in dp.keys():
        return dp[n]
    else:
        if n % 2 == 0:
            dp[n] = (recur(n // 2)**2 + (2 * recur(n // 2 - 1)) * recur(n//2)) % 1000000007
            return dp[n]
        else:
            dp[n] = (recur(n//2)**2 + recur(n//2 + 1)**2) % 1000000007
            return dp[n]

print(recur(n))
