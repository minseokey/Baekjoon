import copy
import sys

h,w = map(int,sys.stdin.readline().split())
lis = list(map(int,sys.stdin.readline().split()))

dp = [0 for i in range(w)]

maxx = 0
beforemax = 0
temp = []
water = 0
for i in range(len(lis)):
    # 1. max 보다 클때.
    if maxx <= lis[i]:
        beforemax = maxx
        maxx = lis[i]
        for j in temp:
            water += beforemax - j
        temp = []
    # 2. max 보단 작지만 바로 직전 거보단 클때
    elif maxx > lis[i] > lis[i - 1]:
        for j in range(len(temp)):
            if temp[j] < lis[i]:
                water += lis[i] - temp[j]
                temp[j] = lis[i]

        temp.append(lis[i])

    # 3. 바로 직전거보다 작거나 같을때.
    else:
        temp.append(lis[i])


# 6 6
# 5 4 1 3 1 2
print(water)