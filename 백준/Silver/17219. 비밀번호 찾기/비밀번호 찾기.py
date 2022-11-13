import sys
n,m = map(int,sys.stdin.readline().split())

newdict = dict()
for i in range(n):
    t1,t2 = sys.stdin.readline().split()
    newdict[t1] = t2.strip()
for i in range(m):
    temp = sys.stdin.readline().strip()
    print(newdict[temp])
