import sys
from collections import deque

lisa = list(sys.stdin.readline().strip())
lisb = list(sys.stdin.readline().strip())
# x축 lisb, y축 lisa
dp = [[0 for i in range(len(lisb) + 1)] for _ in range(len(lisa) + 1)]

# lcs 구하기
for i in range(1, len(lisa) + 1):
    for j in range(1, len(lisb) + 1):
        if lisa[i - 1] == lisb[j - 1]:
            dp[i][j] = dp[i-1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j],dp[i][j-1])

print(dp[-1][-1])


ans =[]
x = len(lisb)
y = len(lisa)

while x > 0 and y > 0:
    if dp[y][x] == dp[y-1][x]:
        y -= 1
    elif dp[y][x] == dp[y][x-1]:
        x -= 1
    else:
        ans.append(lisb[x-1])
        x -= 1
        y -= 1

ta = list(reversed(ans))
print("".join(ta))
