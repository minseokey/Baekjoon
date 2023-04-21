import sys
from collections import deque

me, sis = map(int, sys.stdin.readline().split())
queue = deque()
queue.append((me, 0))
fast = float('inf')
count = 0
visited = [False for i in range(100001)]
while queue:
    n, time = queue.popleft()
    visited[n] = True
    if n == sis and fast == float('inf'):
        fast = time
        count += 1
    elif n == sis and time == fast:
        count += 1

    elif time < fast:
        if 0 <= n - 1 <= 100000 and not visited[n-1]:
            queue.append((n - 1, time + 1))
        if 0 <= n + 1 <= 100000 and not visited[n+1]:
            queue.append((n + 1, time + 1))
        if 0 <= n * 2 <= 100000 and not visited[n*2]:
            queue.append((n * 2, time + 1))

print(fast)
print(count)