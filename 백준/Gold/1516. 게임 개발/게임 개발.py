import heapq
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
remain = defaultdict(list)
needs = defaultdict(list)
queue = []

anslis = [0] * (n+1)
time = [0] * (n+1)
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    time[i+1] = tmp[0]
    if len(tmp) == 2:
        heapq.heappush(queue, (tmp[0], i+1))
    for t in tmp[1:len(tmp) - 1]:
        remain[t].append(i+1)
        needs[i+1].append(t)

while queue:
    t, now = heapq.heappop(queue)
    anslis[now] = t

    for nex in remain[now]:
        needs[nex].remove(now)
        if len(needs[nex]) == 0:
            heapq.heappush(queue,(anslis[now] + time[nex], nex))

    remain.pop(now)

for i in range(1,len(anslis)):
    print(anslis[i])

