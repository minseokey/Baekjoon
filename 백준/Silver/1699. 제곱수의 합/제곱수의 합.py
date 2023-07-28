import math
import sys

n = int(sys.stdin.readline())
rtn = math.floor(math.sqrt(n))
lis = [i*i for i in range(1,rtn+1)]
dp = [i for i in range(n+1)]

for i in range(1,len(lis)):
    temp = lis[i]
    for j in range(temp,n+1):
        if j % temp == 0:
            dp[j] = dp[j-temp] + 1
        else:
            dp[j] = min(dp[j-temp] + 1, dp[j])

print(dp[-1])