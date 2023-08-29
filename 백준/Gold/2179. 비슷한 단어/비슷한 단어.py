import copy
import sys

input = sys.stdin.readline
n = int(input())
lis = [input().strip() for i in range(n)]

maxx = -1
anslis = []
for i in range(n):
    for j in range(i + 1, n):
        if lis[i][:maxx + 1] == lis[j][:maxx + 1]:
            key = False
            for k in range(maxx + 1, min(len(lis[i]), len(lis[j]))):
                if lis[i][k] == lis[j][k]:
                    maxx += 1
                    key = True
                else:
                    break
            if key:
                anslis = [lis[i], lis[j]]
if not anslis:
    print(lis[0])
    print(lis[1])
else:
    print(anslis[0])
    print(anslis[1])
