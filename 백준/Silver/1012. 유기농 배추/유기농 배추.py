import sys

t = int(sys.stdin.readline().strip())
DIR = [(0,1), (-1,0), (1,0), (0,-1)]

for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    arr = []
    check = []
    for _ in range (n+1):
        arr.append(([0])*(m+1))
        check.append(([0]) * (m+1))

    for _ in range(k):
        c,r = map(int,sys.stdin.readline().split())
        arr[r][c] = 1

    count = 0
    for i in range(n+1):
        for j in range(m+1):
            # BFS
            if arr[i][j] == 1 and check[i][j] == 0:
                count += 1
                queue = [(i,j)]
                while queue:
                    ty, tx = queue.pop()
                    check[ty][tx] = 1
                    for dy,dx in DIR:
                        if arr[ty+dy][tx+dx] == 1 and check[ty+dy][tx+dx] == 0:
                            queue.append((ty+dy, tx+dx))

    print(count)