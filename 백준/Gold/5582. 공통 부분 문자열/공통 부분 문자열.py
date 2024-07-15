import sys

lis1 = list(sys.stdin.readline().strip())
lis2 = list(sys.stdin.readline().strip())
dp = [[0] * (len(lis2) + 1) for _ in range(len(lis1) + 1)]

for i in range(len(lis1)):
    for j in range(len(lis2)):
        if lis1[i] == lis2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            
maxx = 0

for i in dp:
    maxx = max(maxx, max(i))

print(maxx)