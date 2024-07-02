import heapq
import sys
from collections import deque

n,c = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

dic = dict()
for _ in range(m):
    s,e,w = map(int, sys.stdin.readline().split())
    if s in dic.keys():
        dic[s].append([e,w])
    else:
        dic[s] = [[e,w]]


def cleanqueue():
    global queue
    queue.sort(reverse=True)
    temp = c
    for i in range(len(queue)-1, -1, -1):
        if queue[i][1] < temp:
            temp -= queue[i][1]
        elif temp != 0:
            queue[i][1] = temp
            queue = queue[i:]
            break


ans = 0
queue = []
# 큐 내부의 합이 항상 c가 되도록, 지금 넣는거보다 큰게 있으면 지워주면서
# 맨 뒤의 요소가 가장 작은 요소. reverse = True
for i in range(1, n+1):
    # 배달 먼저
    while queue and queue[-1][0] == i:
        dest, w = queue.pop()
        ans += w

    # 담기
    if i in dic.keys():
        for dest, w in dic[i]:
            queue.append([dest,w])

    # 큐정리
    cleanqueue()


print(ans)