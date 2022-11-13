import sys

sys.setrecursionlimit(5000)
n = int(input())

for i in range(n):
    maxx,maxy,num = map(int,sys.stdin.readline().split())
    lisorigin = [[0 for j in range(maxx)]for k in range(maxy)]
    liscopy = [[0 for j in range(maxx)]for k in range(maxy)]
    lis = []
    for j in range(num):
        pinx,piny = map(int,sys.stdin.readline().split())
        lisorigin[piny][pinx] = 1
        lis.append([piny,pinx])

    def recur(yy,xx):
        liscopy[yy][xx] = 1
        if xx+1 < maxx and liscopy[yy][xx+1] == 0 and lisorigin[yy][xx+1] == 1:
            recur(yy, xx + 1)
        if xx > 0 and liscopy[yy][xx-1] == 0 and lisorigin[yy][xx-1] == 1:
            recur(yy, xx - 1)
        if yy+1 < maxy and liscopy[yy+1][xx] == 0 and lisorigin[yy+1][xx] == 1:
            recur(yy + 1, xx)
        if yy > 0 and liscopy[yy-1][xx] == 0 and lisorigin[yy-1][xx] == 1:
            recur(yy - 1, xx)
        else:
            return

    bug = 0
    for i in lis:
        if liscopy[i[0]][i[1]] == 0:
            recur(i[0],i[1])
            bug += 1
    print(bug)