# 연속 -> 할인
import sys
from collections import deque

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = deque([int(sys.stdin.readline()) for _ in range(n)])

maxx = 0
temp = deque()
for i in range(k):
    tt = sushi.popleft()
    temp.append(tt)
    sushi.append(tt)

while sushi:
    count = len(set(temp))
    if c not in temp:
        count += 1

    maxx = max(count, maxx)

    temp.append(sushi.popleft())
    temp.popleft()

print(maxx)


