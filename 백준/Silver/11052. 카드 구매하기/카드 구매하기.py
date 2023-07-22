import sys

n = int(sys.stdin.readline())

lis = [0]+list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(n+1)]

# ind ==> 개수, num ==> 가격
for i in range(1,n+1):
    for j in range(i,n+1):
        dp[j] = max(dp[j-i] + lis[i],dp[j])


print(dp[n])







