import sys
n = int(sys.stdin.readline().strip())
lis = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
dp[0] = lis[0]
for i in range(1,len(lis)):
    dp[i] = max(dp[i-1]+lis[i],lis[i])
print(max(dp))
