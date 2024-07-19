import sys

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n+1)

for ran in range(n + 1):
    temp_max = 0
    for alr in range(ran):
        temp_max = max(temp_max, dp[alr] + max(lis[alr:ran]) - min(lis[alr:ran]))
    dp[ran] = temp_max

print(dp[-1])