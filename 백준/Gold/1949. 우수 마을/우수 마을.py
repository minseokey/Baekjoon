import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

# 옆에있는 마을 우수마을 X
# 우수마을 최대로
# 우수마을이 안된 마을은 우수마을과 마주봐야한다.
# dp를 두줄로 유지?

lis = list(map(int, sys.stdin.readline().split()))
lis = lis
dp = [[0, 0] for _ in range(n)]  # 앞은 우수 마을이 아닐때, 뒤는 우수마을일때

road = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    road[a].append(b)
    road[b].append(a)

queue = deque([0])
visited = [False] * n

def backtrack(now):
    if not visited[now]:
        visited[now] = True

        me = []
        not_me = []
        temp = []
        for nex in road[now]:
            if not visited[nex]:
                backtrack(nex)
                temp.append(nex)
            me.append(dp[nex][1])
            not_me.append(max(dp[nex]))

        dp[now][0] += (sum(me) + lis[now])
        dp[now][1] += sum(not_me)

backtrack(0)
ansl = []
for i in dp:
    ansl.append(max(i))

print(max(ansl))

