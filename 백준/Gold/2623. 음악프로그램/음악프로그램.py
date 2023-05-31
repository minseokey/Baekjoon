import sys
from collections import deque

sing, pd = map(int, sys.stdin.readline().split())
topo = [0 for _ in range(sing + 1)]
dic = dict()

for _ in range(pd):
    tmp = list(map(int, sys.stdin.readline().split()))
    leng = tmp[0]
    tmp = tmp[1:]
    for i in range(leng - 1):
        if tmp[i] in dic.keys():
            dic[tmp[i]].append(tmp[i + 1])
        else:
            dic[tmp[i]] = [tmp[i + 1]]
        topo[tmp[i+1]] += 1

# queue init
queue = deque()
ans = []

for i in range(1,sing+1):
    if topo[i] == 0:
        queue.append(i)
        ans.append(i)

while queue:
    tmp = queue.popleft()
    if tmp in dic.keys():
        for i in dic[tmp]:
            topo[i] -= 1
            if topo[i] == 0:
                queue.append(i)
                ans.append(i)
        dic.pop(tmp)


if len(ans) == sing:
    for i in ans:
        print(i)
else:
    print(0)