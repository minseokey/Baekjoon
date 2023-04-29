import sys

origin = [1,1,2,2,2,8]
input = list(map(int,sys.stdin.readline().split()))

for i in range(6):
    origin[i] = origin[i] - input[i]

print(*origin)