import sys
from collections import deque

y, x = map(int, sys.stdin.readline().split())

lis = [sys.stdin.readline().split() for i in range(y)]
lis[0][0] = "A"


# 초반 공기층 처리
def airing():
    queue = deque()
    queue.append([0, 0])
    visit = [[False for a in range(x)] for b in range(y)]
    visit[0][0] = True
    while queue:
        tempy, tempx = queue.popleft()
        if tempy + 1 < y and not visit[tempy + 1][tempx] and lis[tempy + 1][tempx] in ["0", "A"]:
            lis[tempy + 1][tempx] = "A"
            visit[tempy + 1][tempx] = True
            queue.append([tempy + 1, tempx])
        if tempx + 1 < x and not visit[tempy][tempx + 1] and lis[tempy][tempx + 1] in ["0", "A"]:
            lis[tempy][tempx + 1] = "A"
            visit[tempy][tempx + 1] = True
            queue.append([tempy, tempx + 1])
        if tempy - 1 > 0 and not visit[tempy - 1][tempx] and lis[tempy - 1][tempx] in ["0", "A"]:
            lis[tempy - 1][tempx] = "A"
            visit[tempy - 1][tempx] = True
            queue.append([tempy - 1, tempx])
        if tempx - 1 > 0 and not visit[tempy][tempx - 1] and lis[tempy][tempx - 1] in ["0", "A"]:
            lis[tempy][tempx - 1] = "A"
            visit[tempy][tempx - 1] = True
            queue.append([tempy, tempx - 1])


# 치즈 녹이기
def recur():
    templis = []
    for i in range(y):
        for j in range(x):
            if lis[i][j] == "1":
                count = 0
                if i > 0 and lis[i - 1][j] == "A":
                    count += 1
                if j > 0 and lis[i][j - 1] == "A":
                    count += 1
                if i < y - 1 and lis[i + 1][j] == "A":
                    count += 1
                if j < x + 1 and lis[i][j + 1] == "A":
                    count += 1

                if count >= 2:
                    templis.append([i, j])
    for a, b in templis:
        lis[a][b] = "A"


def check():
    for i in lis:
        for j in i:
            if j != "A":
                return False
    return True


ans = 0
while True:
    airing()
    recur()
    ans += 1
    if check():
        break

print(ans)
