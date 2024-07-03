from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
m = len(str(n))


def swap(num, i, j):
    newnum = list(str(num))
    if i == 0 and newnum[j] == '0':
        return False
    newnum[i], newnum[j] = newnum[j], newnum[i]
    return int("".join(newnum))


# set을 이용한 visited
visited = [set() for _ in range(k)]
hq = deque([(k, n)])

ans = -1
while hq:
    kk, nn = hq.popleft()
    if kk == 0:
        if nn > ans:
            ans = nn

    else:
        for i in range(m):
            for j in range(i + 1, m):
                # i가 0일때 nn[j] == 0 이면 안된다.
                swapans = swap(nn, i, j)
                if swapans and swapans not in visited[kk-1]:
                    hq.append((kk - 1, swapans))
                    visited[kk-1].add(swapans)

print(ans)
