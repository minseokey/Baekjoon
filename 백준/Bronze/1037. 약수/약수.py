import sys

n = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))
print(max(lis) * min(lis))