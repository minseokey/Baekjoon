# 일단 위상정렬이 베이스다.
# 근데 큐를 사용하는것이 아닌 우선순위 큐로 풀어주어야 한다 (난이도가 작은 순서대로)
import heapq
import sys

n,m = map(int,sys.stdin.readline().split())

dic = dict()
leftaft = [0 for i in range(n+1)]
for i in range(n+1):
    dic[i] =[]

for i in range(m):
    bef,aft = map(int,sys.stdin.readline().split())
    dic[bef].append(aft)
    leftaft[aft] += 1

zerolis = []
for i in range(1,len(leftaft)):
    if leftaft[i] == 0:
        heapq.heappush(zerolis,i)

ans = []
while zerolis:
    temp = heapq.heappop(zerolis)
    ans.append(temp)
    for i in dic[temp]:
        leftaft[i] -= 1
        if leftaft[i] == 0:
            heapq.heappush(zerolis,i)
print(*ans)