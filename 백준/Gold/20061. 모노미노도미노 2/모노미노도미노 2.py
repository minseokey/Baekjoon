import sys

n = int(sys.stdin.readline())

# t1 -> 1*1, t2 -> 1*2(가로), t3 -> 2*1(세로)

score = 0

# 4*6 x 축 0,1
green = [[False] * 4 for _ in range(6)]
# 6*4 y 축 0,1
blue = [[False] * 4 for _ in range(6)]


def move(block, typ, color):
    global score
    # green 이 기준이다.
    if typ == 1:  # 하나블록
        x = block[0][1]
        key = True
        for y in range(5):
            if not color[y][x] and color[y+1][x]:
                color[y][x] = True
                key = False
                break
        if key:
            color[5][x] = True

    if typ == 2:  # 가로블록
        x1 = block[0][1]
        x2 = block[1][1]
        key = True
        for y in range(5):
            if not color[y][x1] and not color[y][x2] and color[y+1][x1] or color[y+1][x2]:
                color[y][x1] = True
                color[y][x2] = True
                key = False
                break
        if key:
            color[5][x1] = True
            color[5][x2] = True

    if typ == 3:  # 세로블록
        x = block[0][1]
        key = True
        for y in range(4):
            if not color[y][x] and not color[y + 1][x] and color[y+2][x]:
                color[y][x] = True
                color[y + 1][x] = True
                key = False
                break
        if key:
            color[4][x] = True
            color[5][x] = True

    # 한줄삭제 및 점수추가
    now = 2
    while now < 6:
        if color[now].count(True) == 4:
            color.pop(now)
            color.insert(0, [False] * 4)
            score += 1
        else:
            now += 1

    ## error
    # 남는거 삭제
    count = 0
    for i in range(2):
        if color[i].count(False) != 4:
            count += 1

    for _ in range(count):
        color.pop()
        color.insert(0, [False] * 4)

    # if color == green:
    #     for i in color:
    #         print(i)
    #     print()

    # if color == blue:
    #     for i in color:
    #         print(i)
    #     print()

    return color


for i in range(n):
    t, y, x = map(int, sys.stdin.readline().split())
    block_blue = [(x, 3-y)]
    block_green = [(y, x)]
    if t == 2:
        block_green.append((y,x + 1))
        block_blue.append((x+1, 3-y))
    if t == 3:
        block_green.append((y + 1, x))
        block_blue.append((x, 3 - (y+1)))
    green = move(block_green, t, green)

    if t == 3:
        t = 2
    elif t == 2:
        t = 3

    blue = move(block_blue, t, blue)

print(score)
ans = 0
for i in range(4):
    for j in range(6):
        if blue[j][i]:
            ans += 1
        if green[j][i]:
            ans += 1

print(ans)
