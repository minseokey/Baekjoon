# 순서
# 1. 좋아하는 학생이 주변에 많은 칸.
# 2. 빈칸이 많은 칸.
# 3. 행의 번호 -> 열의 번호가 작은 칸.
# 만족도 = 10 ** (좋아하는 학생의 수 - 1) (만약 좋아하는 사람 0 -> 0)
import sys


def sitdown(stu):
    candidate = []
    # iter.0 -> 전체 빈칸
    for i in range(n):
        for j in range(n):
            if school_map[i][j] == 0:
                candidate.append([i, j, 0, 0])

    # iter.1 -> 좋아하는 아이 수
    for i in candidate:
        for j in DIR:
            if 0 <= i[0] + j[0] < n and 0 <= i[1] + j[1] < n and school_map[i[0] + j[0]][i[1] + j[1]] in likedict[stu]:
                i[2] += 1
    candidate.sort(key=lambda x: x[2], reverse=True)
    maxx = candidate[0][2]
    for j in candidate[::-1]:
        if j[2] < maxx:
            candidate.pop()
        else:
            break

    # iter.2 -> 빈자리의 수
    for i in candidate:
        for j in DIR:
            if 0 <= i[0] + j[0] < n and 0 <= i[1] + j[1] < n and school_map[i[0] + j[0]][i[1] + j[1]] == 0:
                i[3] += 1
    candidate.sort(key=lambda x: x[3], reverse=True)
    maxx = candidate[0][3]
    for j in candidate[::-1]:
        if j[3] < maxx:
            candidate.pop()
        else:
            break

    # iter.3 -> 행, 열이 작은것 pick
    candidate.sort()
    school_map[candidate[0][0]][candidate[0][1]] = stu


n = int(sys.stdin.readline())
likedict = {}
for _ in range(n ** 2):
    tlis = list(map(int, sys.stdin.readline().split()))
    likedict[tlis[0]] = tlis[1:]

school_map = [[0] * n for _ in range(n)]
DIR = ([0, 1], [0, -1], [1, 0], [-1, 0])
ans = 0
for num in likedict.keys():
    sitdown(num)

# 만족도 조사
for i in range(n):
    for j in range(n):
        temp = 0
        for ty,tx in DIR:
            if 0 <= i+ty < n and 0 <= j+tx <n and school_map[i+ty][j+tx] in likedict[school_map[i][j]]:
                temp += 1

        if temp > 0:
            ans += 10 ** (temp-1)
print(ans)