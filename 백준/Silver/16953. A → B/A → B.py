import itertools
import sys
from collections import deque

start,end = map(int,sys.stdin.readline().split())

ans = False
qu = deque()
qu.append((start,1))
while qu:
    k,fois = qu.popleft()
    if k == end:
        ans = fois
        break
    if k < end:
        qu.append((k*2,fois+1))
        qu.append((int(str(k)+"1"),fois+1))

if ans == False:
    print(-1)
else:
    print(ans)