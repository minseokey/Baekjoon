import sys

n,m = map(int,sys.stdin.readline().split())
lis = []
wall = []
cam = []
for i in range(n):
    temp = sys.stdin.readline().split()
    for j in range(m):
        if temp[j] != "0":
            if temp[j] == "6":
                wall.append((i,j))
            else:
                cam.append((temp[j],i,j))
    lis.append(temp)

cam.sort()
ans = 64
# 북 동 남 서 순서
DIR = [(-1,0),(0,1),(1,0),(0,-1)]

def countt(lis):
    ccount = 0
    for i in lis:
        for k in i:
            if k == "0":
                ccount += 1
    return ccount

def move(d,y,x):
    dy = DIR[d][0]
    dx = DIR[d][1]
    mlis = []
    while True:
        if n > dy+y >= 0 and m > dx+x >= 0 and (lis[dy+y][dx+x] == "0"):
            lis[dy+y][dx+x] = "#"
            mlis.append((dy+y,dx+x))
            y += dy
            x += dx
        elif n > dy+y >= 0 and m > dx+x >= 0 and lis[dy+y][dx+x] != "6":
            y += dy
            x += dx
        else:
            break

    return mlis

def backmove(liss):
    for dy,dx in liss:
        lis[dy][dx] = "0"


def recur(c):
    global ans
    if c == len(cam):
        ans = min(ans, countt(lis))
        return
    w,y,x = cam[c]
    if w == "1":
        dirlis = [(0), (1), (2), (3)]
    elif w == "2":
        dirlis = [(0, 2), (1, 3)]
    elif w == "3":
        dirlis = [(0, 1), (1, 2), (2, 3), (3, 0)]
    elif w == "4":
        dirlis = [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]
    elif w == "5":
        dirlis = [(0, 1, 2, 3)]

    if w == "1":
        for j in dirlis:
            temp = move(j,y,x)
            recur(c+1)
            backmove(temp)
    else:
        for i in dirlis:
            temp = []
            for j in i:
                temp += move(j,y,x)
            recur(c+1)
            backmove(temp)

recur(0)
print(ans)





