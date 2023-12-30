import sys

lis = [i + 1 for i in range(20)]

for i in range(10):
    s, e = map(int, sys.stdin.readline().split())
    s -= 1
    e -= 1
    temp = lis[s:e+1]
    temp.reverse()
    k = 0
    for j in range(s, e + 1):
        lis[j] = temp[k]
        k += 1
print(*lis)
