import sys

r,c = map(int, sys.stdin.readline().split())
lis = [list(sys.stdin.readline().strip()) for _ in range(r)]

DIR = [-1,0,1]

def dfs(y,x):
    if x == c-1:
        return True
    else:
        for i in DIR:
            t = i+y
            if not 0 <= t < r:
                continue
            if lis[t][x+1] == "x":
                continue
            lis[t][x+1] = "x"
            if dfs(t, x+1):
                return True

for i in range(r):
    dfs(i,0)
ans = 0
for i in range(r):
    if lis[i][c-1] == "x":
        ans += 1
print(ans)