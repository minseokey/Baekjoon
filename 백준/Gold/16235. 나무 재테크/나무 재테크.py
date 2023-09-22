import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

field = [[5 for _ in range(n)] for _ in range(n)]
Alis = []
tree = [[deque() for _ in range(n)] for _ in range(n)]

dir8 = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

for i in range(n):
    Alis.append(list(map(int, sys.stdin.readline().split())))

for i in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    tree[y][x].append(z)


# 사계절 구현
# 봄 -> 나이만큼 양분을 먹고 나이가 1 증가.
# 여름 -> 봄에 죽은 나무가 양분으로 변화, 죽은 나무마다 나이를 2로 나눈 값 //.
# 가을 -> 나무가 번식, 번식하려면 5의 배수여야함, 인접한 8개 범위에 1짜리 나무 생성.
# 겨울 -> 땅에 Alis 에 해당하는 양분 공급.

def spring_summer():
    for i in range(n):
        for j in range(n):
            t = 0
            key = True
            while t < len(tree[i][j]):
                if field[i][j] >= tree[i][j][t]:
                    field[i][j] -= tree[i][j][t]
                    tree[i][j][t] += 1
                    t += 1
                else:
                    key = False
                    break

            if not key:
                for _ in range(len(tree[i][j])-1,t-1,-1):
                    field[i][j] += (tree[i][j].pop()//2)

def fall_winter():
    for i in range(n):
        for j in range(n):
            field[i][j] += Alis[j][i]
            for k in tree[i][j]:
                if k % 5 == 0:
                    for dy, dx in dir8:
                        if 0 <= i + dy < n and 0 <= j + dx < n:
                            tree[i + dy][j + dx].appendleft(1)

for i in range(k):
    spring_summer()
    fall_winter()

ans = 0
for i in tree:
    for j in i:
        if j:
            ans += len(j)
print(ans)
