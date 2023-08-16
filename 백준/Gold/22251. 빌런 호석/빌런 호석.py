import sys

n, k, p, x = sys.stdin.readline().split()

lis = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
       [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
       [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
       [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
       [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
       [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
       [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
       [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
       [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
       [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]

ans = 0
origin = ((int(k) - len(str(x))) * ['0']) + list(str(x))
for i in range(int(k)):
    origin[i] = int(origin[i])

for i in range(1,int(n) + 1):
    num = i
    # now 구하기
    now = []
    for j in range(int(k) - 1, -1, -1):
        now.append(num // (10 ** j))
        num %= 10 ** j

    temp = 0
    for j in range(int(k)):
        temp += lis[now[j]][origin[j]]

    if temp <= int(p) and temp != 0:
        ans += 1

print(ans)