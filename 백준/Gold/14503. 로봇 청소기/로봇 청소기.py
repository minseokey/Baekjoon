import sys

ny, mx = map(int, sys.stdin.readline().split())
y, x, direc = map(int, sys.stdin.readline().split())

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

lis = [list(map(int, sys.stdin.readline().split())) for _ in range(ny)]

now = [y, x, direc]
connting = 0

while True:
    # 1번
    yy,xx,ddir = now
    if lis[yy][xx] == 0:
        lis[yy][xx] = 2
        connting += 1

    # 3
    key = False
    for i in DIR:
        if lis[yy + i[0]][xx + i[1]] == 0:
            key = True

    # 3-1
    # 0 -> [3,2,1,0]
    # 1 -> [0,3,2,1]
    # 2 -> [1,0,3,2]
    # 3 -> [2,1,0,3]
    if key:
        for i in range(1, 5):
            ndir = ddir - i
            if ndir < 0:
                ndir += 4
            if lis[yy + DIR[ndir][0]][xx + DIR[ndir][1]] == 0:
                now = [yy + DIR[ndir][0], xx + DIR[ndir][1], ndir]
                break
    else:  # 2-1
        if lis[yy - DIR[ddir][0]][xx - DIR[ddir][1]] == 1:
            break
        else:
            # 2-2
            now = [yy - DIR[ddir][0], xx - DIR[ddir][1], ddir]


print(connting)