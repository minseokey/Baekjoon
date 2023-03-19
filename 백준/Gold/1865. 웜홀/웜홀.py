import sys
from collections import Counter

tc = int(sys.stdin.readline())

for i in range(tc):
    node, vertex, warm = map(int, sys.stdin.readline().split())
    lis = []
    for j in range(vertex):
        temp = list(map(int, sys.stdin.readline().split()))
        lis.append((temp[0], temp[1], temp[2]))
        lis.append((temp[1], temp[0], temp[2]))
    for k in range(warm):
        temp = list(map(int, sys.stdin.readline().split()))
        lis.append((temp[0], temp[1],-temp[2]))

    # 시작지점
    key = False

    dist = [10001 for q in range(node+1)]
    dist[1] = 0
    for e in range(node):
        for v in range(vertex * 2 + warm):
            now = lis[v][0]
            next = lis[v][1]
            weight = lis[v][2]
            if dist[next] > dist[now] + weight:
                dist[next] = dist[now] + weight
                if e == node - 1:
                    key = True

    if not key:
        print("NO")
    else:
        print("YES")
