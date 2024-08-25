import sys
from collections import deque

field = deque([list(sys.stdin.readline().strip()) for _ in range(8)])
DIR = [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
queue = deque()


def nextone():
    field.pop()
    field.appendleft(["."] * 8)


queue.append(((7, 0), 0))
visited = [[False] * 8 for _ in range(8)]
t_lis = 0
key = False

while queue:
    now, ind = queue.popleft()
    if ind > t_lis:
        t_lis += 1
        nextone()
        visited = [[False] * 8 for _ in range(8)]  # Clear

    # 벽에 있는 칸이라면 경우의수 제와
    if field[now[0]][now[1]] == ".":
        if now[0] == 0 and now[1] == 7:
            key = True
            break

        y, x = now[0], now[1]
        for dy, dx in DIR:
            if 0 <= dy + y < 8 and 0 <= dx + x < 8 and field[dy+y][dx+x] != "#" and not visited[dy+y][dx+x]:
                queue.append(((dy + y, dx + x), ind + 1))
                visited[dy+y][dx+x] = True

print(1) if key else print(0)
