import sys
from collections import deque

n = int(sys.stdin.readline())
lis = []
for i in range(n):
    lis.append(sys.stdin.readline().strip())

ans = deque()


def recur(N, lis):
    if len(lis[0]) == 1:
        ans.append(lis[0][0])
        return

    key = True
    prime = lis[0][0]
    for i in range(N):
        for j in range(N):
            if lis[i][j] != prime:
                key = False
                break
        if not key:
            break

    if key:
        ans.append(prime)
        return
    else:
        ans.append("(")
        for o in range(2):
            for j in range(2):
                newlis = [q[(N // 2) * j:(N // 2) * (j + 1)] for q in lis[(N // 2) * o: (N // 2) * (o + 1)]]
                recur(N // 2, newlis)
        ans.append(")")
recur(n,lis)

print("".join(ans))