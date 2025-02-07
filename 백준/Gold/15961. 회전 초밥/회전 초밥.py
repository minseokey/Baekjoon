import sys
from collections import deque, Counter

n, d, k, c = map(int, sys.stdin.readline().split())

maxx = 0
shusi = deque()
tmp = deque()
len_count = [0] * (d+1)
len_count[c] += 1
cnt = 1

for _ in range(k):
    t = int(sys.stdin.readline())
    shusi.append(t)
    tmp.append(t)
    if len_count[t] == 0:
        cnt += 1
    len_count[t] += 1
    maxx = max(cnt, maxx)

for _ in range(n-k):
    t = shusi.popleft()
    len_count[t] -= 1
    if len_count[t] == 0:
        cnt -= 1

    tt = int(sys.stdin.readline())
    shusi.append(tt)
    if len_count[tt] == 0:
        cnt += 1
    len_count[tt] += 1
    maxx = max(cnt, maxx)

# 한바퀴 돌고나서
for _ in range(k):
    t = shusi.popleft()
    len_count[t] -= 1
    if len_count[t] == 0:
        cnt -= 1

    tt = tmp.popleft()
    shusi.append(tt)
    if len_count[tt] == 0:
        cnt += 1
    len_count[tt] += 1
    maxx = max(cnt, maxx)



print(maxx)




