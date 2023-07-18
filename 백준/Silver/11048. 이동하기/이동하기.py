import sys

n,m = map(int,sys.stdin.readline().split())
lis = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        temp = [0]
        if i != 0:
            temp.append(lis[i-1][j])
        if j != 0:
            temp.append(lis[i][j-1])
        if i != 0 and j != 0:
            temp.append(lis[i-1][j-1])

        lis[i][j] += max(temp)

print(lis[-1][-1])