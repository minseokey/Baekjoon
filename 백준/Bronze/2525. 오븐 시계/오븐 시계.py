import sys

a,b = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline())

b+=t
while b >= 60:
    b -= 60
    a += 1
if a >= 24:
    a -= 24
print(a,b)
