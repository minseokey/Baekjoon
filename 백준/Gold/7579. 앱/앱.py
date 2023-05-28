import sys

n,m = map(int,sys.stdin.readline().split())
memory = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

maxnum = sum(price)
# 2차원 dp 제작.

lis = [[0] * (maxnum+1) for _ in range(n+1)]
ans = float('inf')

for i in range(1, n + 1):
    nm = memory[i-1]
    np = price[i-1]

    for j in range(maxnum+1):
        if j >= np:
            lis[i][j] = max(lis[i-1][j],  lis[i-1][j-np] + nm)
        else:
            lis[i][j] = lis[i-1][j]

        if lis[i][j] >= m:
            ans = min(j,ans)

print(ans)




