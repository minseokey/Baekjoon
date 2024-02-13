import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
dic = dict()
# 형식 ->  숫자 : [시작위치들]
lis = list(map(int,sys.stdin.readline().split()))
last = 0
now = 0
maxx = -1
for ind, i in enumerate(lis):
    if i not in dic.keys():
        dic[i] = deque([ind])
    else:
        dic[i].append(ind)
        if len(dic[i]) > k:
            maxx = max(ind - last, maxx)
            now = dic[i].popleft()+1
            last = max(now,last)
maxx = max(n - last, maxx)
print(maxx)