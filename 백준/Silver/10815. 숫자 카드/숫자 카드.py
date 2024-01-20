import bisect
import sys

n = int(sys.stdin.readline())
lis_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
lis_m = list(map(int, sys.stdin.readline().split()))

lis_n.sort()

ans = []
for i in lis_m:
    tt = bisect.bisect_left(lis_n, i)
    if tt < len(lis_n) and lis_n[bisect.bisect_left(lis_n, i)] == i:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)