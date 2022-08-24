import sys
n,m = map(int,sys.stdin.readline().split())

see = set()
listen = set()
for i in range(n):
    see.add(sys.stdin.readline().rstrip())
for i in range(m):
    listen.add(sys.stdin.readline().rstrip())
answer = list(see.intersection(listen))
print(len(answer))
for i in sorted(answer):
    print(i)
