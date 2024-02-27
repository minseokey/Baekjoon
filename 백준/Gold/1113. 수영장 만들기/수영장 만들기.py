import copy
import sys

n, m = map(int, sys.stdin.readline().split())
real_field = []

for i in range(n):
    temp = list(sys.stdin.readline().strip())
    for j in range(m):
        temp[j] = int(temp[j])
    real_field.append(temp)
t = copy.deepcopy(real_field)

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(1, 10):
    for y in range(n):
        for x in range(m):
            if real_field[y][x] >= i:  # 채울 필요가 없다
                pass
            else:
                stack = [(y, x)]  # 주변 검색해서 나보다 작은게 없다면? -> 올리면 된다.
                visited = [[False] * m for _ in range(n)]
                visited[y][x] = True
                key = True
                while stack and key:
                    ty, tx = stack.pop()
                    for dy, dx in DIR:
                        if 0 <= ty + dy < n and 0 <= tx + dx < m:
                            if real_field[ty+dy][tx+dx] < i:
                                if not visited[ty+dy][tx+dx]:
                                    stack.append((ty + dy, tx + dx))
                                    visited[ty+dy][tx+dx] = True
                        else:
                            key = False

                if key:
                    real_field[y][x] = i

ans = 0
for i in range(n):
    ans += sum(real_field[i]) - sum(t[i])

print(ans)