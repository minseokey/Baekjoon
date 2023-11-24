import sys

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

count = 0
for i in lis:
    now = i - b
    count += 1
    if now > 0:
        count += now // c
        if now % c != 0:
            count += 1

print(count)
