import heapq
import sys

n = int(sys.stdin.readline())
open_door = tuple(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
want = []
for _ in range(m):
    want.append(int(sys.stdin.readline()))

# 열려있는문을 옮겨보자.

queue = [(0,0,open_door)]

minn = float('inf')
while queue:
    now, ind, door = heapq.heappop(queue)
    if ind == m:
        minn = min(now, minn)
    elif now > minn:
        break
    else:
        heapq.heappush(queue, (now + abs(door[0] - want[ind]), ind + 1, (want[ind], door[1]))) # door0 를 이동
        heapq.heappush(queue, (now + abs(door[1] - want[ind]), ind + 1, (door[0], want[ind]))) # door1 을 이동

print(minn)