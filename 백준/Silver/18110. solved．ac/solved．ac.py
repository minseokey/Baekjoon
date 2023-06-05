import math
import statistics

n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))

def rnd(num):
    if num % 1 < 0.5:
        return int(num // 1)
    else:
        return int(num // 1) + 1

rid = rnd(n * 0.15)
lis.sort()
ans = 0
for i in range(rid,len(lis) - rid):
    ans += lis[i]

if len(lis) - (rid*2):
    print(rnd(ans/(len(lis) - (rid * 2))))
else:
    print(0)
