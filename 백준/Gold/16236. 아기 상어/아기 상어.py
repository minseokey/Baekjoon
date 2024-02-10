
import sys

n = int(sys.stdin.readline())
lis = []
x, y = 0, 0
for i in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    if 9 in t:
        y = len(lis)
        x = t.index(9)
    lis.append(t)

# initial
lis[y][x] = 0
size = 2
ev_count = 2
move = 0

while True:
    check = [[False for i in range(n)] for j in range(n)]
    queue = [(y, x, move)]
    check[y][x] = True
    key = False

    while queue:
        temp = queue.pop(0)
        # eat
        if 0 < lis[temp[0]][temp[1]] < size:
            lis[temp[0]][temp[1]] = 0
            ev_count -= 1
            if not ev_count:
                size += 1
                ev_count = size
            y = temp[0]
            x = temp[1]
            move = temp[2]
            key = True
            break

        # pass
        else:
            if temp[0] > 0 and lis[temp[0] - 1][temp[1]] <= size and not check[temp[0] - 1][temp[1]]:
                check[temp[0] - 1][temp[1]] = True
                queue.append((temp[0] - 1, temp[1], temp[2] + 1))

            if temp[1] > 0 and lis[temp[0]][temp[1] - 1] <= size and not check[temp[0]][temp[1] - 1]:
                check[temp[0]][temp[1] - 1] = True
                queue.append((temp[0], temp[1] - 1, temp[2] + 1))

            if temp[1] < n - 1 and lis[temp[0]][temp[1] + 1] <= size and not check[temp[0]][temp[1] + 1]:
                check[temp[0]][temp[1] + 1] = True
                queue.append((temp[0], temp[1] + 1, temp[2] + 1))

            if temp[0] < n - 1 and lis[temp[0] + 1][temp[1]] <= size and not check[temp[0] + 1][temp[1]]:
                check[temp[0] + 1][temp[1]] = True
                queue.append((temp[0] + 1, temp[1], temp[2] + 1))

        queue.sort(key=lambda t: (t[2],t[0],t[1]))


    # for i in lis:
    #     print(i)
    # print(move)
    # print('\n')
    if not key:
        print(move)
        break

