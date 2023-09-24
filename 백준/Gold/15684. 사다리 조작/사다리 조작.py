import sys

n, m, h = map(int, sys.stdin.readline().split())
road = [[0] * (n - 1) for _ in range(h)]
empty = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    road[a - 1][b - 1] = 1

for i in range(h):
    for j in range(n - 1):
        if not road[i][j]:
            empty.append((i, j))


# 통과인지 아닌지.
def detector():
    # road 0 -> 0과 1에 길이 있다.
    # road 1 -> 1과 2에 길이 있다.
    # road 2 -> 2과 3에 길이 있다.
    # road 3 -> 3과 4에 길이 있다.
    key = True
    for i in range(n):
        now = i
        for j in range(h):
            if now == 0:
                if road[j][0] == 1:
                    now += 1
            elif now == n - 1:
                if road[j][n - 2] == 1:
                    now -= 1
            else:
                if road[j][now - 1] == 1:
                    now -= 1
                elif road[j][now] == 1:
                    now += 1

        if now != i:
            key = False
            return False
    if key:
        return True


# 지금 현재 카운터에는 empty 의 인덱스에 해당하는 녀석들이 들어있다.
# 이를 이용해 중복없이 만들기.
# 초기 설정.

temp = []
while True:
    if len(temp) > 3:
        print(-1)
        break

    for i in temp:
        ty, tx = empty[i]
        road[ty][tx] = 1

    if detector():
        print(len(temp))
        break

    else:
        # 원상복구
        for j in temp:
            ty, tx = empty[j]
            road[ty][tx] = 0

        if not temp:
            temp = [0]
        else:
            addition = True
            getback = False
            gbn = 0
            maxx = len(empty) - 1
            for i in range(len(temp)):
                if temp[i] < maxx:
                    temp[i] += 1
                    addition = False
                    if i != 0:
                        getback = True
                        gbn = i
                    break
                else:
                    maxx -= 1

            if getback:
                for k in range(gbn - 1, -1, -1):
                    temp[k] = temp[k + 1] + 1

            if addition:
                temp = [i for i in range(len(temp), -1, -1)]

            # 예외처리
            if len(temp) > len(empty):
                print(-1)
                break
