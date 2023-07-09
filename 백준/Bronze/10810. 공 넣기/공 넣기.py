import sys

n,m = map(int,sys.stdin.readline().split())
lis = [0 for i in range(n)]

for i in range(m):
    s,e,inp = map(int,sys.stdin.readline().split())
    for k in range(s-1,e):
        lis[k] = inp

print(*lis)
