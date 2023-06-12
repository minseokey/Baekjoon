import sys

# R => 격자 row, C=> 격자 column, M => 상어 수
R, C, M = map(int, sys.stdin.readline().split())

# 0 위 1 아래 2 오른 3 왼
DEST = [[-1, 0], [1, 0], [0, 1], [0, -1]]
lis = [[[] for _ in range(C)] for _ in range(R)]
shark = []
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    # r,c 위치 s 속력, d 이동방향, z 크기
    lis[r - 1][c - 1].append([d - 1, s, z])
    shark.append([r - 1, c - 1])


def calcpos(y, x):
    td, ts, tz = lis[y][x].pop(0)
    # 최종 이동 위치 계산
    mv = [DEST[td][0] * ts, DEST[td][1] * ts]
    # 2c -2,2r -2 로 나누면 방향, 같은 위치로 이동 가능.
    # 경계선 넘어가면 방향이 바뀐다.
    # 위아래 이동
    if mv[0] != 0:
        tk = abs(mv[0]) % (2 * (R - 1))
        # 끝부분에 방향이 걸칠때 고치고 loop:
        if td == 0 and y == 0:
            td = 1
        if td == 1 and y == R-1:
            td = 0
        while tk > 0:
            # 위
            if td == 0:
                y -= 1
                if y == 0:
                    td = 1
            # 아래
            else:
                y += 1
                if y == R - 1:
                    td = 0
            tk -= 1
    # 죄우 이동
    elif mv[1] != 0:
        tk = abs(mv[1]) % (2 * (C - 1))
        if td == 2 and x == C-1:
            td = 3
        if td == 3 and x == 0:
            td = 2
            
        while tk > 0:
            # 오른쪽
            if td == 2:
                x += 1
                if x == C - 1:
                    td = 3
            # 왼쪽
            else:
                x -= 1
                if x == 0:
                    td = 2
            tk -= 1

    lis[y][x].append([td, ts, tz])
    return y, x


ans = 0
# 상어아저씨 => 0 - C 의 시간을 가진다.
# 1. i => 지금 상어아저씨 위치.
for i in range(C):

    # 2. 상어 잡기
    for j in range(R):
        if lis[j][i]:
            ans += lis[j][i][0][2]
            lis[j][i] = []
            shark.remove([j, i])
            break

    # 3. 상어 이동
    for j, s in enumerate(shark):
        ny, nx = calcpos(s[0], s[1])
        shark[j] = [ny, nx]

    # 4. 같은자리 상어 정리
    for j in range(R):
        for k in range(C):
            if len(lis[j][k]) > 1:
                for i in range(len(lis[j][k]) - 1):
                    shark.remove([j, k])
                lis[j][k] = [max(lis[j][k], key=lambda x: x[2])]

print(ans)
