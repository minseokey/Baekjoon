import copy
import sys

r, c = map(int, sys.stdin.readline().split())
lis = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(r)]
r -= 1
c -= 1
leftlis = copy.deepcopy(lis)
rightlis = copy.deepcopy(lis)

# y-x 를 기준으로 -> right
# y+x 를 기준으로 -> left

# /
for i in range(r + c + 1):
    ystart = i if i <= r else r
    xstart = i - ystart
    # x += 1, y -= 1
    while r >= ystart >= 0 and c >= xstart >= 0:
        if leftlis[ystart][xstart] == 1:
            if 0 <= ystart + 1 <= r and 0 <= xstart - 1 <= c:
                leftlis[ystart][xstart] += leftlis[ystart + 1][xstart - 1]
        ystart -= 1
        xstart += 1

# \
for i in range(r, -(c+1), -1):
    ystart = r if r-i <= c else c+i
    xstart = ystart - i
    while r >= ystart >= 0 and c >= xstart >= 0:
        if rightlis[ystart][xstart] == 1:
            if 0 <= ystart + 1 <= r and 0 <= xstart + 1 <= c:
                rightlis[ystart][xstart] += rightlis[ystart + 1][xstart + 1]
        ystart -= 1
        xstart -= 1

maxdia = 0
for y in range(r + 1):
    for x in range(c + 1):
        # 양 끝점의 left right 값이 모두 같다? -> 다이아.
        able = min(leftlis[y][x], rightlis[y][x])
        move = able - 1
        key = True
        while move+1 > maxdia and key:
            if move+1 > maxdia:
                ly, lx = y+move, x+move
                ry, rx = y+move, x-move
                if 0 <= ly <= r and 0 <= lx <= c and 0 <= ry <= r and 0 <= rx <= c:
                    if leftlis[ly][lx] >= move+1 and rightlis[ry][rx] >= move+1:
                        maxdia = move + 1
                        key = False
            move -= 1
    if r-y < (maxdia-1) * 2 + 1:
        break

print(maxdia)