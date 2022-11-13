import sys

n = int(sys.stdin.readline())
lis = []
for i in range(n):
    lis.append(int(sys.stdin.readline()))
kk = sorted(lis)
for i in kk:
    print(i)
