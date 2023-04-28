import copy
import math
import sys

n,fois = map(int,sys.stdin.readline().split())
lis = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
templis = copy.deepcopy(lis)

dplis = []
dplis.append(lis)


def recur(a,b):
    newlis = [[0 for i in range(n)] for j in range(n)]
    for r in range(n):
        for c in range(n):
            temp = 0
            for k in range(n):
                temp += (a[k][c] * b[r][k])
            if temp >= 1000:
                newlis[r][c] = temp % 1000
            else:
                newlis[r][c] = temp
    return newlis


if fois == 1:
    for i in lis:
        for j in range(len(i)):
            i[j] %= 1000
        print(*i)
else:
    for i in range(1,int(math.log2(fois)) + 1):
        templis = recur(templis,templis)
        dplis.append(templis)


    ske = dplis[0] if fois % 2 == 1 else dplis[1]
    for i in range(len(dplis)-1,-1,-1):
        if 2**i < fois:
            fois -= 2**i
            ske = recur(ske,dplis[i])
            if fois <= 2:
                break

    for i in ske:
        print(*i)

