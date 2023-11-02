import itertools
import sys

ining = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(ining)]
max_score = 0

# 여기서 타자 세팅, 1번 선수는 4번타자이다.
order = [0] * 9
t = itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8], 8)
for i in t:
    lis = []
    for j in range(len(i)):
        lis.append(i[j])
        if j == 2:
            lis.append(0)

    # lis는 타순
    # 항상 유지
    score = 0
    hitter = 0

    for j in range(ining):
        # 라운드별 초기화
        count = 3
        base = [0, 0, 0]
        while count > 0:

            if hitter >= 9:
                hitter = 0

            elif game[j][lis[hitter]] == 0:
                count -= 1
                hitter += 1
            elif game[j][lis[hitter]] == 1:
                b0 = base[0]
                b1 = base[1]
                b2 = base[2]

                base[0] = 1
                base[1] = b0
                base[2] = b1
                score += b2
                hitter += 1
            elif game[j][lis[hitter]] == 2:
                b0 = base[0]
                b1 = base[1]
                b2 = base[2]

                base[0] = 0
                base[1] = 1
                base[2] = b0
                score += (b1 + b2)
                hitter += 1
            elif game[j][lis[hitter]] == 3:
                b0 = base[0]
                b1 = base[1]
                b2 = base[2]

                base[0] = 0
                base[1] = 0
                base[2] = 1
                score += (b0 + b1 + b2)
                hitter += 1
            elif game[j][lis[hitter]] == 4:
                b0 = base[0]
                b1 = base[1]
                b2 = base[2]
                base[0], base[1], base[2] = 0, 0, 0
                score += (b0 + b1 + b2 + 1)
                hitter += 1

    if score > max_score:
        max_score = score

print(max_score)