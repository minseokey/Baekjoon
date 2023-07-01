import sys

lis = list(map(int, sys.stdin.readline().split()))

# node = (a,b) : k 형식
# 만약 있는데 하나가 더 들어오면 min 값만 살아남음

dic = [[[float("inf") for _ in range(5)] for _ in range(5)] for _ in range(len(lis))]
dic[-1][0][0] = 0
n = len(lis) - 1

dd = {(0,0) : 1,(0, 1):2, (0, 2):2, (0, 3):2, (0, 4):2, (1, 1):1, (1, 2):3, (1, 3):4, (1, 4):3,  (2, 1):3, (2, 2):1, (2, 3):3,
           (2, 4):4, (3, 1):4, (3, 2):3, (3, 3):1, (3, 4):3, (4, 1):3, (4, 2):4, (4, 3):3, (4, 4):1,(1,0):2,(2,0):2,(3,0):2,(4,0) : 2}




for i in range(n):
    nownode = lis[i]
    # 오른발
    for j in range(5):  # 멈춘 왼발
        for k in range(5):  # 이동하는 오른발의 원래위치
            addit = dd[(nownode, k)]
            dic[i][j][nownode] = min(dic[i][j][nownode], dic[i - 1][j][k] + addit)

    # 왼발
    for j in range(5):  # 멈춘 오른발
        for k in range(5):  # 이동하는 왼발
            addit = dd[(nownode, k)]
            dic[i][nownode][j] = min(dic[i][nownode][j], dic[i - 1][k][j] + addit)

ans = 100000000000
for i in range(5):
    ans = min(ans,min(dic[n-1][i]))

print(ans)