import heapq
import sys

n = int(sys.stdin.readline())
lis = []
start, end = [], []
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    for j in range(n):
        if temp[j] == "#" and start == []:
            start = [i, j]
        elif temp[j] == "#":
            end = [i, j]
    lis.append(temp)

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[[False] * 4 for _ in range(n)] for _ in range(n)]

d = []
for i in range(4):
    ty, tx = start[0] + DIR[i][0], start[1] + DIR[i][1]
    if 0 <= ty < n and 0 <= tx < n and lis[ty][tx] in [".", "!", "#"]:
        d.append(i)
        break

hqueue = []
for i in d:
    heapq.heappush(hqueue, (0, start[0], start[1], i))
    visited[start[0]][start[1]][i] = True

while hqueue:
    count, ty, tx, d = heapq.heappop(hqueue)
    if [ty, tx] == end:
        print(count)
        break

    if not lis[ty][tx] == "*":
        dy, dx = DIR[d][0], DIR[d][1]
        if 0 <= ty + dy < n and 0 <= tx + dx < n and not visited[ty + dy][tx + dx][d]:
            visited[ty + dy][tx + dx][d] = True
            heapq.heappush(hqueue, (count, ty + dy, tx + dx, d))

        if lis[ty][tx] == "!":
            ld, ldy, ldx = (d+1) % 4, DIR[(d+1) % 4][0], DIR[(d+1) % 4][1]
            rd, rdy, rdx = (d-1) % 4, DIR[(d-1) % 4][0], DIR[(d-1) % 4][1]
            if 0 <= ty + ldy < n and 0 <= tx + ldx < n and not visited[ty + ldy][tx + ldx][ld]:
                visited[ty + ldy][tx + ldx][ld] = True
                heapq.heappush(hqueue, (count + 1, ty + ldy, tx + ldx, ld))

            if 0 <= ty + rdy < n and 0 <= tx + rdx < n and not visited[ty + rdy][tx + rdx][rd]:
                visited[ty + rdy][tx + rdx][rd] = True
                heapq.heappush(hqueue, (count + 1, ty + rdy, tx + rdx, rd))
