import copy
import sys
from collections import deque

ymax, xmax = map(int, sys.stdin.readline().split())

all = []

# wallis[0] => y
# wallis[1] => x

wallis = []
for i in range(ymax):
    temp = []
    for k in sys.stdin.readline().strip():
        temp.append(int(k))
    for j in range(len(temp)):
        if temp[j] == 1:
            wallis.append([i, j])
    all.append(temp)

ans = float('inf')


def nobreak(lis):
    global ans
    queue = deque()
    queue.append((0, 0, 1))
    visited = [[False for i in range(xmax)] for j in range(ymax)]
    visited[0][0] = True

    while queue:
        y, x, c = queue.popleft()
        if y == ymax - 1 and x == xmax - 1:
            ans = min(ans, c)

        if y < ymax - 1 and not visited[y + 1][x] and lis[y + 1][x] == 0:
            visited[y + 1][x] = True
            queue.append((y + 1, x, c + 1))

        if y > 0 == lis[y - 1][x] and not visited[y - 1][x]:
            visited[y - 1][x] = True
            queue.append((y - 1, x, c + 1))

        if x < xmax - 1 and not visited[y][x + 1] and lis[y][x + 1] == 0:
            visited[y][x + 1] = True
            queue.append((y, x + 1, c + 1))

        if x > 0 == lis[y][x - 1] and not visited[y][x - 1]:
            visited[y][x - 1] = True
            queue.append((y, x - 1, c + 1))


def wallbreak(lis):
    global ans
    queue = deque()
    queue.append((0, 0, 1, False))
    lis[0][0] = 2

    while queue:
        # for i in lis:
        #     print(i)
        # print('\n')

        # 2 => 벽 안뚫은 길
        # 3 => 벽 뚫은 길

        y, x, c, b = queue.popleft()
        # print(y,x,c,b)
        if y == ymax - 1 and x == xmax - 1:
            ans = min(ans, c)
            break

        if y < ymax - 1:

            # 길이 있으니까 가는길이야
            if lis[y + 1][x] == 0:
                if b:
                    lis[y+1][x] = 3
                else:
                    lis[y+1][x] = 2
                queue.append((y + 1, x, c + 1, b))

            # 벽을 부숨
            elif lis[y + 1][x] == 1 and not b:
                queue.append((y + 1, x, c + 1, True))

            # 아직 벽을 부수지는 않았지만, 벽을 부순거 보다는 느린 길이야
            elif lis[y+1][x] == 3 and not b:
                lis[y+1][x] = 2
                queue.append((y + 1, x, c + 1, b))

        if y > 0:

            if lis[y - 1][x] == 0:
                if b:
                    lis[y-1][x] = 3
                else:
                    lis[y-1][x] = 2
                queue.append((y - 1, x, c + 1, b))

            elif lis[y - 1][x] == 1 and not b:
                queue.append((y - 1, x, c + 1, True))

            elif lis[y-1][x] == 3 and not b:
                lis[y-1][x] = 2
                queue.append((y-1, x, c + 1, b))

        if x < xmax - 1:

            if lis[y][x + 1] == 0:
                if b:
                    lis[y][x+1] = 3
                else:
                    lis[y][x+1] = 2
                queue.append((y, x + 1, c + 1, b))

            elif lis[y][x + 1] == 1 and not b:
                queue.append((y, x + 1, c + 1, True))

            elif lis[y][x+1] == 3 and not b:
                lis[y][x+1] = 2
                queue.append((y, x + 1, c + 1, b))

        if x > 0:

            if lis[y][x - 1] == 0:
                if b:
                    lis[y][x-1] = 3
                else:
                    lis[y][x-1] = 2
                queue.append((y, x - 1, c + 1, b))

            elif lis[y][x - 1] == 1 and not b:
                queue.append((y, x - 1, c + 1, True))

            elif lis[y][x-1] == 3 and not b:
                lis[y][x-1] = 2
                queue.append((y, x - 1, c + 1, b))


all2 = copy.deepcopy(all)
nobreak(all)
wallbreak(all2)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
