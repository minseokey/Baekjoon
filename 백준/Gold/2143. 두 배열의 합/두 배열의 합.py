import bisect
import sys

t = int(sys.stdin.readline())
al = int(sys.stdin.readline())
lisa = list(map(int, sys.stdin.readline().split()))
bl = int(sys.stdin.readline())
lisb = list(map(int, sys.stdin.readline().split()))

dpa = []
for i in range(al):
    startnum = lisa[i]
    for j in range(i, al):
        if i == j:
            dpa.append(startnum)
        elif i < j:
            startnum += lisa[j]
            dpa.append(startnum)

dpb = []
for i in range(bl):
    startnum = lisb[i]
    for j in range(i, bl):
        if i == j:
            dpb.append(startnum)
        elif i < j:
            startnum += lisb[j]
            dpb.append(startnum)

dpa.sort()
dpb.sort()
ans = 0

dpaset = list(set(dpa))
dpaset.sort()

for i in dpaset:
    bst = bisect.bisect_left(dpb, t - i)
    ben = bisect.bisect_right(dpb, t - i)
    if bst - ben != 0:
        ast = bisect.bisect_left(dpa, i)
        aen = bisect.bisect_right(dpa, i)

        ans += (aen - ast) * (ben - bst)

print(ans)
