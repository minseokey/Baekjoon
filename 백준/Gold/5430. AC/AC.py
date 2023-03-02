import sys
from collections import deque

n = int(sys.stdin.readline().strip())
for i in range(n):
    order = sys.stdin.readline().strip()
    length = int(sys.stdin.readline().strip())
    k = True
    rev = True

    if length == 0:
        a = sys.stdin.readline()
        lis = []
    else:
        lis = deque(map(int, sys.stdin.readline().strip("]\n[ ").split(",")))

    for j in order:
        if j == "R":
            rev = not rev
        elif j == "D" and len(lis) == 0:
            print("error")
            k = False
            break
        elif j == "D" and len(lis) > 0 and rev:
            lis.popleft()
        elif j == "D" and len(lis) > 0 and not rev:
            lis.pop()

    if k and rev:
        a = "["
        for q in lis:
            a += str(q) + ","
        if len(a) > 1:
            a = a[:-1]
        a += "]"
        print(a)
    if k and not rev:
        a = "["
        for q in reversed(lis):
            a += str(q) + ","
        if len(a) > 1:
            a = a[:-1]
        a += "]"
        print(a)