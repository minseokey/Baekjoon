import copy
import sys
from collections import deque

fois = int(sys.stdin.readline())
for i in range(fois):
    N,K = map(int,sys.stdin.readline().split())
    timer = list(map(int,sys.stdin.readline().split()))
    dic = {}
    for i in range(N):
        dic[i] = []
    for i in range(K):
        st, en = map(int,sys.stdin.readline().split())
        dic[en - 1].append(st - 1)

    target = int(sys.stdin.readline())
    ans = 0
    visited = [False for i in range(N)]
    timedp = copy.deepcopy(timer)

    #맨앞 찾아주기
    def front():
        lis = deque()
        for i in dic.keys():
            if not dic[i] and not visited[i]:
                lis.append(i)
                visited[i] = True
        return lis

    # 맨 앞과 연결 된걸 빼고, 해당시점에서의 시간 계산.
    def removenode(node):
        for i in dic.keys():
            if node in dic[i]:
                dic[i].remove(node)
                timedp[i] = max(timer[i] + timedp[node],timedp[i])


    queue = front()
    for i in queue:
        visited[i] = True

    while True:
        while queue:
            temp = queue.popleft()
            removenode(temp)

        queue = front()
        if target - 1 in queue:
            break
        elif False not in visited:
            break

    print(timedp[target-1])
