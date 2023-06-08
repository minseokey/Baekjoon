import sys

my, mx = map(int, sys.stdin.readline().split())
lis = [list(sys.stdin.readline().strip()) for _ in range(my)]
DEST = [[0, -1], [0, 1], [-1, 0], [1, 0]]

# 최대 dp 깊이 수
ans = 1

def backT(vAlp, y, x, count):
    global ans
    ans = max(count, ans)
    for ty, tx in DEST:
        if 0 <= ty + y < my and 0 <= tx + x < mx:
            if vAlp[ord(lis[ty+y][tx+x]) - 65] == False:
                vAlp[ord(lis[ty+y][tx+x]) - 65] = True
                backT(vAlp, y + ty, x + tx, count + 1)
                vAlp[ord(lis[ty+y][tx+x]) - 65] = False


ordlis = [False] * 26
ordlis[ord(lis[0][0]) - 65] = True

backT(ordlis, 0, 0, 1)
print(ans)
