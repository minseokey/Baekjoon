import heapq
import sys

t = int(sys.stdin.readline())
k = 0
while t != 0:
    k += 1
    lis = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
    visited = [[float('inf') for _ in range(t)] for _ in range(t)]

    # 우선순위큐, bfs, visited map 활용, 더 작으면 update
    queue = []
    queue.append([0, 0, lis[0][0]])
    visited[0][0] = lis[0][0]
    while queue:
        ty, tx, tnum = heapq.heappop(queue)
        if ty > 0:
            if visited[ty - 1][tx] > visited[ty][tx] + lis[ty - 1][tx]:
                visited[ty - 1][tx] = visited[ty][tx] + lis[ty - 1][tx]
                queue.append([ty - 1, tx, visited[ty - 1][tx]])
        if tx > 0:
            if visited[ty][tx - 1] > visited[ty][tx] + lis[ty][tx - 1]:
                visited[ty][tx-1] = visited[ty][tx] + lis[ty][tx-1]
                queue.append([ty, tx-1, visited[ty][tx-1]])
        if ty < t - 1:
            if visited[ty + 1][tx] > visited[ty][tx] + lis[ty + 1][tx]:
                visited[ty + 1][tx] = visited[ty][tx] + lis[ty + 1][tx]
                queue.append([ty + 1, tx, visited[ty + 1][tx]])
        if tx < t - 1:
            if visited[ty][tx + 1] > visited[ty][tx] + lis[ty][tx + 1]:
                visited[ty][tx + 1] = visited[ty][tx] + lis[ty][tx + 1]
                queue.append([ty, tx + 1, visited[ty][tx + 1]])

    print("Problem {}: {}".format(k, visited[-1][-1]))

    t = int(sys.stdin.readline())
