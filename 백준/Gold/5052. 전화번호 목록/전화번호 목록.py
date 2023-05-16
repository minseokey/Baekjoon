import sys

fois = int(sys.stdin.readline())
for i in range(fois):
    n = int(sys.stdin.readline())
    lis = []
    for j in range(n):
        lis.append(sys.stdin.readline().strip())
    lis.sort()
    key = True
    for a in range(len(lis) - 1):
        if lis[a] == lis[a+1][:len(lis[a])]:
            print("NO")
            key = False
            break

    if key:
        print("YES")
