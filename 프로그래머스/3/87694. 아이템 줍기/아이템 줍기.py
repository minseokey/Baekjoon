import heapq


def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[0] * 102 for _ in range(102)]

    # 테두리 1
    for dy, dx, uy, ux in rectangle:
        for y in range(dy * 2, uy * 2 + 1):
            for x in [dx * 2, ux * 2]:
                field[y][x] = 1
        for x in range(dx * 2, ux * 2 + 1):
            for y in [dy * 2, uy * 2]:
                field[y][x] = 1
    # 안쪽 2
    for dy, dx, uy, ux in rectangle:
        for y in range(dy * 2 + 1, uy * 2):
            for x in range(dx * 2 + 1, ux * 2):
                field[y][x] = 2

    queue = [(0, characterX * 2, characterY * 2)]
    visited = [[False] * 102 for _ in range(102)]
    DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    while queue:
        cnt, ty, tx = heapq.heappop(queue)
        if ty == itemX * 2 and tx == itemY * 2:
            return cnt // 2
        if not visited[ty][tx]:
            visited[ty][tx] = True
            for dy, dx in DIR:
                if 0 <= ty + dy < 102 and 0 <= tx + dx < 102 and not visited[ty + dy][tx + dx] and field[ty + dy][tx + dx] == 1:
                    heapq.heappush(queue, (cnt + 1, ty + dy, tx + dx))
