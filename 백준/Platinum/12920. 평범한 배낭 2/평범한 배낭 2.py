import sys

n,m = map(int,sys.stdin.readline().split())
al = 0
stuff = []
for _ in range(n):
    v,c,k = map(int,sys.stdin.readline().split())
    i = 1
    while k > 0:
        take = min(k, i)
        stuff.append((v * take, c * take))
        k -= take
        i *= 2

al = len(stuff)
dp = [[0] * (m+1) for _ in range(al + 1)]
stuff.sort()


for i in range(1, al + 1):
    for j in range(m + 1):
        if j >= stuff[i - 1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-stuff[i-1][0]] + stuff[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])