import sys
from collections import deque

y, x = map(int, sys.stdin.readline().split())
lis = [list(sys.stdin.readline().strip()) for _ in range(y)]
startblue = []
startred = []

for i in range(y):
    for j in range(x):
        if lis[i][j] == "R":
            startred = [i, j]
            lis[i][j] = "."
        elif lis[i][j] == "B":
            startblue = [i, j]
            lis[i][j] = "."

# 상하좌우 방햫
DIREC = [[1, 0], [-1, 0], [0, -1], [0, 1]]
ans = -1

visited = [[[[False for _ in range(x)] for _ in range(y)] for _ in range(x)]for _ in range(y)]
# 큐에 저장되어아 하는 내용 => 블루의 y,x 레드의 y,x, 카운터 최대 10
queue = deque()
queue.append([startred, startblue, 1])

visited[startred[0]][startred[1]][startblue[0]][startblue[1]] = True
anskey = False

while queue and not anskey:
    tred, tblue, tcnt = queue.popleft()
    visited[tred[0]][tred[1]][tblue[0]][tblue[1]] = True
    for direc in DIREC:

        tnred = [tred[0],tred[1]]
        tnblue = [tblue[0],tblue[1]]

        # 구멍에 들어갔는지 여부
        keyred = False
        keyblue = False
        # 벽에 막혔는지 여부
        blkred = False
        blkblue = False

        # 둘중 하나라도 앞이 막히지 않았을때
        while not blkred or not blkblue:
            if not blkred:
                # 빨강 전진
                tnred[0] += direc[0]
                tnred[1] += direc[1]
                # 똑같은 점에 위치한다면 하나 멈추고 다음꺼 기다린다.
                if tnred == tnblue:
                    # 끝이 벽일때
                    if lis[tnred[0] + direc[0]][tnred[1] + direc[1]] == "#" and not keyblue:
                        blkred = True
                    elif keyblue:
                        blkred = True
                        keyred = True
                    tnred[0] -= direc[0]
                    tnred[1] -= direc[1]
                elif lis[tnred[0]][tnred[1]] == 'O':
                    keyred = True
                    blkred = True
                elif lis[tnred[0]][tnred[1]] == "#":
                    blkred = True
                    tnred[0] -= direc[0]
                    tnred[1] -= direc[1]

            if not blkblue:
                # 파랑 전진
                tnblue[0] += direc[0]
                tnblue[1] += direc[1]
                if tnred == tnblue:
                    # 해당 방향의 끝일때.
                    if lis[tnblue[0] + direc[0]][tnblue[1] + direc[1]] == "#" and not keyred:
                        blkblue = True
                    elif keyred:
                        blkblue = True
                        keyblue = True
                    tnblue[0] -= direc[0]
                    tnblue[1] -= direc[1]
                elif lis[tnblue[0]][tnblue[1]] == 'O':
                    keyblue = True
                    blkblue = True
                elif lis[tnblue[0]][tnblue[1]] == "#":
                    blkblue = True
                    tnblue[0] -= direc[0]
                    tnblue[1] -= direc[1]


        # 빨간건 들어가고, 파란건 안들어갔을때. => 정답
        if keyred and not keyblue:
            ans = tcnt
            anskey = True
            break
        # 파란거 들어감 => 무시
        elif keyblue:
            continue
        # 나머지 => 다음 무브 계산
        else:
            if not visited[tnred[0]][tnred[1]][tnblue[0]][tnblue[1]]:
                if tcnt <= 9:
                    queue.append([tnred,tnblue,tcnt+1])


print(ans)