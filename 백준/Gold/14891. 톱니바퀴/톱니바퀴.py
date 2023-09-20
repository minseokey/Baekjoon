import sys

lis = [list(sys.stdin.readline().strip()) for _ in range(4)]
# 2,6,2,6,2,6,...
n = int(sys.stdin.readline())


def move(direction, motor):
    # 시계
    if direction == 1:
        temp = lis[motor].pop()
        lis[motor] = [temp] + lis[motor]
    # 반시계
    else:
        temp = lis[motor].pop(0)
        lis[motor].append(temp)


for i in range(n):
    start, direc = map(int, sys.stdin.readline().split())
    start -= 1
    rotate = [[start,direc]]
    r = start
    rd = direc
    for j in range(start+1,4):
        rd = -rd
        if lis[r][2] != lis[j][6]:
            rotate.append([j, rd])
            r = j
        else:
            break

    l = start
    ld = direc
    for j in range(start-1,-1,-1):
        ld = -ld
        if lis[l][6] != lis[j][2]:
            rotate.append([j,ld])
            l = j
        else:
            break

    for j in rotate:
        move(j[1],j[0])


ans = 0
for i in range(4):
    if lis[i][0] == "1":
        ans += 2**i

print(ans)
