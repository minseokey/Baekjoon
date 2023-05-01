import sys
from collections import deque

node,ques = map(int,sys.stdin.readline().split())
lis = [[0 for i in range(node)] for j in range(node)]
dic = dict()

for i in range(node - 1):
    start,end,weight = map(int,sys.stdin.readline().split())

    if start-1 in dic.keys():
        dic[start-1].append([end-1,weight])
    else:
        dic[start-1] = [[end-1,weight]]

    if end-1 in dic.keys():
        dic[end-1].append([start-1,weight])
    else:
        dic[end-1] = [[start-1,weight]]


def bfs(no):
    lenlis = [float('inf') for _ in range(node)]
    queue = deque()
    queue.append(no)
    visit = [False for _ in range(node)]
    visit[no] = True
    while queue:
        temp = queue.popleft()
        for tn,tw in dic[temp]:
            if not visit[tn]:
                lenlis[tn] = min(tw,lenlis[temp])
                visit[tn] = True
                queue.append(tn)

    return lenlis

anslis = [False for i in range(node)]
for i in range(ques):
    limit,tnode = map(int,sys.stdin.readline().split())
    ans = 0
    if not anslis[tnode-1]:
        tempkk = bfs(tnode - 1)
        for j in tempkk:
            if j != float('inf') and j >= limit:
                ans += 1
        anslis[tnode-1] = tempkk
    else:
        for j in anslis[tnode-1]:
            if j != float('inf') and j >= limit:
                ans += 1
    print(ans)