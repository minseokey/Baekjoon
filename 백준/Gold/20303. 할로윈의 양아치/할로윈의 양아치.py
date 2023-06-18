import sys
import collections
read = sys.stdin.readline

children_N, relationship_N, resonance = map(int, read().strip().split())

candy_list = [0] + list(map(int, read().strip().split()))
friend_list = [[] for _ in range(children_N + 1)]
for _ in range(relationship_N):
    a, b = map(int, read().strip().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

visited = [0] * (children_N + 1)
def bfs(x):
    group = [[x], candy_list[x]]
    queue = collections.deque()
    queue.append(x)
    visited[x] = 1

    while queue:
        now_x = queue.popleft()

        for i in range(len(friend_list[now_x])):
            if visited[friend_list[now_x][i]] == 0:
                friend = friend_list[now_x][i]
                visited[friend] = 1
                queue.append(friend)
                group[0].append(friend)
                group[1] += candy_list[friend]

    return group


children_group = []
for i in range(1, children_N + 1):
    if visited[i] == 0:
        children_group.append(bfs(i))
children_group = [0] + children_group

dp = [[0] * (resonance + 1) for _ in range(len(children_group))]
for i in range(1, len(children_group)):
    children, candy = len(children_group[i][0]), children_group[i][1]
    for reso in range(1, resonance + 1):
        if reso <= children:
            dp[i][reso] = dp[i - 1][reso]
        else:
            dp[i][reso] = max(dp[i - 1][reso - children] + children_group[i][1], dp[i - 1][reso])

print(dp[-1][-1])