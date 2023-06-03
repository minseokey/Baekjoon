import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
dic = dict()
lis = [0 for _ in range(n+1)]
for i in range(1,n+1):
    dic[i] = []
for i in range(m):
    f,l = map(int,sys.stdin.readline().split())
    dic[f].append(l)
    lis[l] += 1

queue = deque()
ans = []
for i in range(1,len(lis)):
    if lis[i] == 0:
        queue.append(i)
        ans.append(i)

while queue:
    now = queue.popleft()
    if now in dic.keys():
        for i in dic[now]:
            lis[i] -= 1
            if lis[i] == 0:
                queue.append(i)
                ans.append(i)
        dic.pop(now)




print(*ans)