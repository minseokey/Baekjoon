import heapq
import sys

n, m, k = map(int, sys.stdin.readline().split())
field = [list(sys.stdin.readline().strip()) for _ in range(n)]
target = sys.stdin.readline().strip()

DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
wordlen = len(target) - 1
dp = [[[0] * (wordlen + 1) for _ in range(m)] for _ in range(n)]


def dfs(dfslis):
    queue = dfslis
    count = 0
    visited = [[[False] * (wordlen+1) for _ in range(m)] for _ in range(n)]
    for c, y, x in dfslis:
        dp[y][x][-c] = 1
        visited[y][x][-c] = True
    while queue:
        t, ny, nx = heapq.heappop(queue)
        t = -t
        if t == 0:
            count += dp[ny][nx][0]
        else:
            for dy, dx in DIR:
                for i in range(1, k + 1):
                    tty, ttx = dy * i + ny, dx * i + nx

                    if 0 <= tty < n and 0 <= ttx < m and field[tty][ttx] == target[t - 1] and not visited[tty][ttx][t-1]:
                        dp[tty][ttx][t - 1] += dp[ny][nx][t]
                        heapq.heappush(queue, (-t + 1, tty, ttx))
                        visited[tty][ttx][t-1] = True
                    elif 0 <= tty < n and 0 <= ttx < m and field[tty][ttx] == target[t - 1]:
                        dp[tty][ttx][t - 1] += dp[ny][nx][t]


    return count


temp = []
for i in range(n):
    for j in range(m):
        # target 의 역순으로 돌자.
        if field[i][j] == target[-1]:
            temp.append((-wordlen, i, j))

print(dfs(temp))
