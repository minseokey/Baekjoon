import sys
import bisect

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
ans = []

for i in lis:
    if not ans or i > ans[-1]:
        ans.append(i)
    else:
        ans[bisect.bisect_left(ans, i, 0, len(ans))] = i

print(len(ans))