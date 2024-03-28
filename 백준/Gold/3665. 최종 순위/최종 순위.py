import sys
from collections import deque

fois = int(sys.stdin.readline())

for _ in range(fois):
    n = int(sys.stdin.readline())
    origin = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    change = set(tuple(map(int, sys.stdin.readline().split())) for _ in range(m))

    before_check = dict()
    for i in range(1, n + 1):
        before_check[i] = []

    # i 가 j 보다 등수가 높다 보장.
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (origin[j], origin[i]) in change or (origin[i], origin[j]) in change:
                before_check[origin[j]].append(origin[i])
            else:
                before_check[origin[i]].append(origin[j])

    # 만약 여기서 위상정렬이 가능하면 답 아니면 impossible
    countlist = []
    queue = deque()
    visited = [False] * (n+1)
    visited[0] = True
    ans = []
    for i in range(1, n+1):
        countlist.append(n - 1 - len(before_check[i]))
        if len(before_check[i]) == n-1:
            queue.append(i)
            ans.append(i)
            visited[i] = True

    while queue:
        temp = queue.popleft()
        for i in before_check[temp]:
            countlist[i-1] -= 1
            if countlist[i-1] == 0:
                queue.append(i)
                ans.append(i)

    if len(ans) != n:
        print("IMPOSSIBLE")
    else:
        print(*ans)

