import sys
from collections import deque

n = int(sys.stdin.readline())

for t in range(n):
    a, b, ans = map(list, sys.stdin.readline().split())

    queue = deque([(0, 0)])
    key = False
    visited = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]

    while queue:
        a_cnt, b_cnt = queue.popleft()

        if not visited[a_cnt][b_cnt]:
            visited[a_cnt][b_cnt] = True

            if a_cnt + b_cnt == len(ans):
                key = True
                break

            if a_cnt < len(a) and ans[a_cnt + b_cnt] == a[a_cnt]:
                queue.append((a_cnt+1, b_cnt))

            if b_cnt < len(b) and ans[a_cnt + b_cnt] == b[b_cnt]:
                queue.append((a_cnt, b_cnt+1))

    if not key:
        print("Data set " + str(t + 1) + ": no")
    else:
        print("Data set " + str(t + 1) + ": yes")