import sys

n, m, l, k = map(int, sys.stdin.readline().split())

# m -> 세로, n -> 가로
lis = []
for i in range(k):
    tx, ty = map(int, sys.stdin.readline().split())
    lis.append((tx, ty))

ans = 0
# 두점을 뽑아 그 두개가 교차하는 한점을 좌 상단으로 잡고 그 내부의 개수 조사 -> 최대값 구하기
for i in range(len(lis)):
    for j in range(i, len(lis)):
        count = 0

        ax, ay = lis[i]
        bx, by = lis[j]

        x = min(ax,bx)
        y = min(ay,by)

        for kx,ky in lis:
            if x <= kx <= x+l and y <= ky <= y+l:
                count += 1

        if count > ans:
            ans = count


print(k - ans)