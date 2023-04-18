import sys

y, x, fois = map(int, sys.stdin.readline().split())
lis = [list(map(int, sys.stdin.readline().split())) for i in range(y)]

upper = 0
lower = 0
for i in range(len(lis)):
    if -1 in lis[i]:
        upper = i
        lower = i + 1
        break


def diffuse():
    newlis = [[0 for a in range(x)] for b in range(y)]

    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if lis[i][j] > 0:
                ori = lis[i][j]
                if j > 0 and lis[i][j - 1] != -1:
                    newlis[i][j - 1] += lis[i][j] // 5
                    ori -= lis[i][j] // 5
                if j < x - 1 and lis[i][j + 1] != -1:
                    newlis[i][j + 1] += lis[i][j] // 5
                    ori -= lis[i][j] // 5
                if i > 0 and lis[i - 1][j] != -1:
                    newlis[i - 1][j] += lis[i][j] // 5
                    ori -= lis[i][j] // 5
                if i < y - 1 and lis[i + 1][j] != -1:
                    newlis[i + 1][j] += lis[i][j] // 5
                    ori -= lis[i][j] // 5
                newlis[i][j] += ori

    return newlis


def onesec():
    lis[upper].insert(1,0)
    lis[lower].insert(1,0)
    tempUp = lis[upper].pop()
    tempDn = lis[lower].pop()
    tempp1, tempp2 = 0,0

    for i in range(upper-1,-1,-1):
        tempp1 = lis[i].pop()
        lis[i].append(tempUp)
        tempUp = tempp1

    for i in range(lower+1,y):
        tempp2 = lis[i].pop()
        lis[i].append(tempDn)
        tempDn = tempp2


    tempUp = lis[0].pop(0)
    tempDn = lis[-1].pop(0)

    lis[0].insert(x-2,tempp1)
    lis[-1].insert(x-2,tempp2)

    for i in range(1,upper):
        tempp1 = lis[i].pop(0)
        lis[i].insert(0,tempUp)
        tempUp = tempp1

    for i in range(y-2,lower,-1):
        tempp2 = lis[i].pop(0)
        lis[i].insert(0,tempDn)
        tempDn = tempp2

    lis[lower][0] = 0
    lis[upper][0] = 0



for i in range(fois):
    lis = diffuse()
    onesec()


ans = 0
for i in lis:
    for j in i:
        ans += j
print(ans)