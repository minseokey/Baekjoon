import sys

n,s = map(int,sys.stdin.readline().split())
lis = list(map(int,sys.stdin.readline().split()))

temp = 0
lis.insert(0,0)
for i in range(len(lis)):
    lis[i] += temp
    temp = lis[i]


short = n
bigkey = False

for i in range(len(lis)):
    start = i
    end = short + i if short + i <= n else n
    key = False
    while True:

        if end >= start and lis[end] - lis[start] >= s:
            end -= 1
            key = True
            bigkey = True
        else:
            if key:
                short = min(end - i + 1,short)
            break

if bigkey:
    print(short)
else:
    print(0)
