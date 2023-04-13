import copy
import sys

n = int(sys.stdin.readline())

maxlis = [0,0,0]
minlis = [0,0,0]
for i in range(n):
    origin = list(map(int,sys.stdin.readline().split()))
    temp = [0,0,0]

    temp[0] = max(maxlis[0], maxlis[1]) + origin[0]
    temp[1] = max(maxlis[0], maxlis[1], maxlis[2]) + origin[1]
    temp[2] = max(maxlis[1], maxlis[2]) + origin[2]
    maxlis[0] = temp[0]
    maxlis[1] = temp[1]
    maxlis[2] = temp[2]

    temp[0] = min(minlis[0], minlis[1]) + origin[0]
    temp[1] = min(minlis[0], minlis[1], minlis[2]) + origin[1]
    temp[2] = min(minlis[1], minlis[2]) + origin[2]
    minlis[0] = temp[0]
    minlis[1] = temp[1]
    minlis[2] = temp[2]

print(max(maxlis),min(minlis))