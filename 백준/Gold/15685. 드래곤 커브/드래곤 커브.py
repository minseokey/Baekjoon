import copy
import sys

DIR = ((0, 1), (-1, 0), (0, -1), (1, 0))


# 피봇을 기준으로 (endy, endx) 피봇 + (피봇 - 원래점) * 방향 => 새로운 점.
# 각 단계후 리스트의 마지막 원소 -> 넥스트 피봇.
def dragon(d_lis, gen):
    global x, y
    if gen == 0:
        return
    l = len(d_lis)
    for i in range(l - 1, -1, -1):
        d = (d_lis[i] + 1) % 4
        y += DIR[d][0]
        x += DIR[d][1]
        lis[y][x] = 1
        d_lis.append(d)

    dragon(d_lis, gen-1)


n = int(sys.stdin.readline())
lis = [[0] * 101 for _ in range(101)]
for i in range(n):
    x, y, d, g = map(int, sys.stdin.readline().split())
    d_lis = [d]
    lis[y][x] = 1
    lis[y+DIR[d][0]][x+DIR[d][1]] = 1
    y += DIR[d][0]
    x += DIR[d][1]
    dragon(d_lis, g)


ans = 0
for i in range(100):
    for j in range(100):
        if lis[i][j] == 1:
            if lis[i+1][j] == 1 and lis[i][j+1] == 1 and lis[i+1][j+1] == 1:
                ans += 1

print(ans)