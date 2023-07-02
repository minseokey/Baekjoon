import bisect
import sys

n = int(sys.stdin.readline())
lis = []
for i in range(n):
    lis.append(list(map(int,sys.stdin.readline().split())))
lis.sort()
lisb = []
for i in lis:
    lisb.append(i[1])

tt = []
for i in lisb:
    ind = bisect.bisect_right(tt,i)
    if ind == len(tt):
        tt.append(i)
    else:
        tt[ind] = i

print(n - len(tt))