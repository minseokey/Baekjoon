import sys

n = int(sys.stdin.readline())

# 2원 5원

field = [0] * (n+1)
if n >= 5:
    field[2] = 1
    field[5] = 1
elif n >= 2:
    field[2] = 1

coin = [2,5]
for i in range(2):
    for j in range(n+1):
        if field[j] != 0 and j+coin[i] <= n:
            field[j+coin[i]] = field[j]+1

if field[-1] == 0:
    print(-1)
else:
    print(field[-1])
