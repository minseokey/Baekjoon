import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
lis = []
for i in range(n):
    lis.append(sys.stdin.readline().strip())

check = [[False for i in range(m)] for j in range(n)]
ans = n * m

count = 0
queue = deque()
queue.append([0, 0, 1])
while queue:

    temp = queue.popleft()

    if temp[0] == n - 1 and temp[1] == m - 1:
        print(temp[2])
        break

    if temp[0] < n-1 and lis[temp[0] + 1][temp[1]] == '1' and not check[temp[0] + 1][temp[1]]:
        check[temp[0] + 1][temp[1]] = True
        queue.append([temp[0] + 1, temp[1], temp[2] + 1])

    if temp[0] > 0 and lis[temp[0] - 1][temp[1]] == '1' and not check[temp[0] - 1][temp[1]]:
        check[temp[0] - 1][temp[1]] = True
        queue.append([temp[0] - 1, temp[1], temp[2] + 1])

    if temp[1] < m-1 and lis[temp[0]][temp[1] + 1] == '1' and not check[temp[0]][temp[1] + 1]:
        check[temp[0]][temp[1] + 1] = True
        queue.append([temp[0], temp[1] + 1, temp[2] + 1])

    if temp[1] > 0 and lis[temp[0]][temp[1] - 1] == '1' and not check[temp[0]][temp[1] - 1]:
        check[temp[0]][temp[1] - 1] = True
        queue.append([temp[0], temp[1] - 1, temp[2] + 1])