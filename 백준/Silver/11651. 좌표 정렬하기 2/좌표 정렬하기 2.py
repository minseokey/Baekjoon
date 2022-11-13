import sys
n = int(input())
lis = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lis.append([b, a])
slis = sorted(lis)
for i in slis:
    print("{} {}".format(i[1], i[0]))