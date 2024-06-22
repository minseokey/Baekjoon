import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preord = list(map(int, sys.stdin.readline().split()))
    inord = list(map(int, sys.stdin.readline().split()))
    postord = []


    def recur(root, in_s, in_e):
        for i in range(in_s, in_e):
            if inord[i] == preord[root]:
                recur(root + 1, in_s, i)
                recur(root + 1 + i - in_s, i + 1, in_e)
                postord.append(preord[root])


    recur(0, 0, n)
    print(*postord)
