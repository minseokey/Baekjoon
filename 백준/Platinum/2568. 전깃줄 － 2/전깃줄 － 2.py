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
dp = [-1 for i in range(n)]
for i,num in enumerate(lisb):
    ind = bisect.bisect_right(tt, num)

    if ind == len(tt):
        tt.append(num)
        dp[i] = tt.index(num)
    else:
        tt[ind] = num
        dp[i] = ind



last = max(dp)
anslis = []
for i in range(len(dp)-1,-1,-1):
    if last == dp[i]:
        last -= 1
    else:
        anslis.append(lis[i])


print(n - len(tt))
anslis.reverse()
for i in anslis:
    print(i[0])


