import bisect
# disect => 정렬이 보장되어야함. O(logN)
import sys

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))

# index =>dp값 1 -> lis값
updatelis = []

dp = [0 for i in range(n)]

maxind = 0
maxdp = 0
for i in range(n):
    if len(updatelis) != 0 and lis[i] <= updatelis[-1]:
        temp = bisect.bisect_left(updatelis, lis[i])
        updatelis[temp] = lis[i]
        dp[i] = temp
    else:
        updatelis.append(lis[i])
        dp[i] = len(updatelis)-1

        if dp[i] > maxdp:
            maxdp = dp[i]
            maxind = i

# maxind 부터 리스트 거꾸로 돌면서 dp에 해당하는 숫자들 갓챠
ans = []

for i in range(maxind,-1,-1):
    if dp[i] == maxdp:
        ans.append(lis[i])
        if maxdp == 0:
            break
        maxdp -= 1


print(len(ans))
print(*reversed(ans))