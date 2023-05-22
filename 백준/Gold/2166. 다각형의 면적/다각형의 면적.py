import sys

n = int(sys.stdin.readline())
lis = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

pro = lis[-1][0] * lis[0][1]
pre = lis[-1][1] * lis[0][0]
for i in range(n-1):
    pro += lis[i][0] * lis[i+1][1]
    pre += lis[i][1] * lis[i+1][0]

print(round(abs(pre - pro) / 2,1))

