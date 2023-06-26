import sys
from collections import deque

y, x = map(int, sys.stdin.readline().split())
lis = []
for i in range(y):
    lis += list(sys.stdin.readline().strip())

uf = [i for i in range(y * x)]
visited = [False for i in range(x * y)]
MAXX = x * y


def find(a):
    if a == uf[a]:
        return a
    return find(uf[a])


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    elif a > b:
        uf[a] = b
        return True
    else:
        uf[b] = a
        return True

count = 0

def dfs(t):
    global count
    queue = deque()
    queue.append(t)

    while queue:
        temp = queue.popleft()
        if not visited[temp]:
            visited[temp] = True

            if lis[temp] == "U":
                if union(temp, temp - x):
                    queue.append(temp - x)
                else:
                    if find(temp - x) == find(t):
                        count += 1

            elif lis[temp] == "D":
                if union(temp, temp + x):
                    queue.append(temp + x)
                else:
                    if find(temp + x) == find(t):
                        count += 1

            elif lis[temp] == "L":
                if union(temp, temp - 1):
                    queue.append(temp - 1)
                else:
                    if find(temp - 1) == find(t):
                        count += 1

            elif lis[temp] == "R":
                if union(temp, temp + 1):
                    queue.append(temp + 1)
                else:
                    if find(temp + 1) == find(t):
                        count += 1


for i in range(MAXX):
    if not visited[i]:
        dfs(i)

print(count)

