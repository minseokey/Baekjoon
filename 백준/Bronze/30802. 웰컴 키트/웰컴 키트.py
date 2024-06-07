import math
import sys

N = int(sys.stdin.readline())
t_lis = list(map(int,sys.stdin.readline().split()))
t,p = map(int,sys.stdin.readline().split())

ans = 0
for i in t_lis:
    ans += math.ceil(i/t)

print(ans)
print(N//p,N%p)

