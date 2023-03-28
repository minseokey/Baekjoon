import copy
import sys

n,m = map(int,sys.stdin.readline().split())
lis = []
for i in range(n):
    lis.append(list(map(int,sys.stdin.readline().split())))


for i in lis:
    temp = 0
    for j in range(n):
        temp += i[j]
        i[j] = temp

for i in range(n):
    temp = 0
    for j in range(n):
        temp += lis[j][i]
        lis[j][i] = temp

# print("\n")
# for i in lis:
#     print(i)

for i in range(m):
    boty,botx,topy,topx = map(int,sys.stdin.readline().split())
    botx -= 1
    boty -= 1
    topy -= 1
    topx -= 1

    if boty > 0 and botx > 0:
        print(lis[topy][topx] + lis[boty-1][botx-1] - lis[boty-1][topx] - lis[topy][botx-1])
    elif boty > 0:
        print(lis[topy][topx] - lis[boty - 1][topx])
    elif botx > 0:
        print(lis[topy][topx] - lis[topy][botx - 1])
    else:
        print(lis[topy][topx])

