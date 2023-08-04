import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())

lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# l 보다크고 r 보다 작을때 인구이동.

ans = 0
# 횟수 반복
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    opengates = []
    for i in range(n):
        for j in range(n):
            # 만약 한점을 딱 잡았을때, 이 점이 전에 방문한적이 없는 점이다?
            if not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                gate = set()
                gate.add((i, j))
                visited[i][j] = True

                while queue:
                    ty, tx = queue.popleft()

                    if ty + 1 < n and not visited[ty + 1][tx]:
                        if l <= abs(lis[ty][tx] - lis[ty + 1][tx]) <= r:
                            visited[ty + 1][tx] = True
                            queue.append((ty + 1, tx))
                            gate.add((ty + 1, tx))

                    if tx + 1 < n and not visited[ty][tx + 1]:
                        if l <= abs(lis[ty][tx] - lis[ty][tx + 1]) <= r:
                            visited[ty][tx + 1] = True
                            queue.append((ty, tx + 1))
                            gate.add((ty, tx + 1))

                    if 0 <= ty - 1 and not visited[ty - 1][tx]:
                        if l <= abs(lis[ty][tx] - lis[ty - 1][tx]) <= r:
                            visited[ty - 1][tx] = True
                            queue.append((ty - 1, tx))
                            gate.add((ty - 1, tx))

                    if 0 <= tx - 1 and not visited[ty][tx - 1]:
                        if l <= abs(lis[ty][tx] - lis[ty][tx - 1]) <= r:
                            visited[ty][tx - 1] = True
                            queue.append((ty, tx - 1))
                            gate.add((ty, tx - 1))

                if len(gate) > 1:
                    opengates.append(gate)

    if len(opengates) == 0:
        break

    else:
        # print(opengates)
        for opens in opengates:
            temp = 0
            for q in opens:
                temp += lis[q[0]][q[1]]

            avg = temp // len(opens)
            for q in opens:
                lis[q[0]][q[1]] = avg

        # for w in lis:
        #     print(w)
        # print("\n")

        ans += 1

print(ans)
