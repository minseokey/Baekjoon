import sys
from collections import deque

n = int(sys.stdin.readline())
dic = dict()

for q in range(n-1):
    ro,of = map(int,sys.stdin.readline().strip().split())
    if of not in dic.keys():
        dic[of] = [ro]
    else:
        dic[of].append(ro)

    if ro not in dic.keys():
        dic[ro] = [of]
    else:
        dic[ro].append(of)

visitednode= [False for i in range(n + 1)]
# 자식 : 부모
ans = [0 for i in range(n-1)]
queue = deque()
queue.append(1)
visitednode[1] = True
while queue:
    temp = queue.popleft()
    if temp in dic.keys():
        for k in dic[temp]:
            if not visitednode[k]:
                queue.append(k)
                ans[k-2] = temp
                visitednode[k] = True

for i in ans:
    print(i)






