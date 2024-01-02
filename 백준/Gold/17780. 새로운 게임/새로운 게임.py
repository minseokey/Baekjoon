import sys

n, k = map(int, sys.stdin.readline().split())
lis_stack = [[[] for _ in range(n)] for _ in range(n)]
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

horse = []
for p in range(k):
    a, b, c = map(int, sys.stdin.readline().split())
    lis_stack[a - 1][b - 1].append(p)
    horse.append([a - 1, b - 1, c])
DIR = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]


# lis -> 0 = 흰색, 1 = 빨강, 2 = 파랑
# horse -> ind0 = y, ind1 = x, ind2 = DIR
# lis_stack -> 실재 스택 모양 그대로

def change_dir(d):
    if d == 2:
        d = 1
    elif d == 1:
        d = 2
    elif d == 3:
        d = 4
    elif d == 4:
        d = 3
    return d


def move(y, x, isblue):
    real_dir = DIR[horse[lis_stack[y][x][0]][2]]
    real_stack = lis_stack[y][x]
    nexty = y + real_dir[0]
    nextx = x + real_dir[1]

    if isblue:
        if nextx >= n or nextx < 0 or nexty >= n or nexty < 0 or lis[nexty][nextx] == 2:
            return y, x
        elif lis[nexty][nextx] == 0:
            lis_stack[nexty][nextx] = lis_stack[nexty][nextx] + real_stack
            lis_stack[y][x] = []
            for j in lis_stack[nexty][nextx]:
                horse[j] = [nexty, nextx, horse[j][2]]
            return nexty, nextx

        elif lis[nexty][nextx] == 1:
            lis_stack[nexty][nextx] = lis_stack[nexty][nextx] + list(reversed(real_stack))
            lis_stack[y][x] = []
            for j in lis_stack[nexty][nextx]:
                horse[j] = [nexty, nextx, horse[j][2]]
            return nexty, nextx


    elif 0 <= nexty < n and 0 <= nextx < n:
        # white
        if lis[nexty][nextx] == 0:
            lis_stack[nexty][nextx] = lis_stack[nexty][nextx] + real_stack
            lis_stack[y][x] = []
            for j in lis_stack[nexty][nextx]:
                horse[j] = [nexty, nextx, horse[j][2]]
            return nexty, nextx
        # red
        elif lis[nexty][nextx] == 1:
            lis_stack[nexty][nextx] = lis_stack[nexty][nextx] + list(reversed(real_stack))
            lis_stack[y][x] = []
            for j in lis_stack[nexty][nextx]:
                horse[j] = [nexty, nextx, horse[j][2]]
            return nexty, nextx

        # blue -> blue 는 이동후 방향을 바꿔 한번 더 움직인다.
        else:
            horse[lis_stack[y][x][0]][2] = change_dir(horse[lis_stack[y][x][0]][2])
            return move(y, x, True)

    else:
        # 넘어가버린 blue
        horse[lis_stack[y][x][0]][2] = change_dir(horse[lis_stack[y][x][0]][2])
        return move(y, x, True)


count = 0
key = False
while not key:
    count += 1
    for i in range(k):
        if lis_stack[horse[i][0]][horse[i][1]][0] == i:
            rety, retx = move(horse[i][0], horse[i][1], False)
            if len(lis_stack[rety][retx]) >= 4:
                key = True
                break
        #
        # for qq in lis_stack:
        #     print(qq)
        # print(count)

    if count == 1001:
        break
if key:
    print(count)
else:
    print(-1)
