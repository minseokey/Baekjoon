import sys

n = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))

lis.sort()

if len(lis) % 2 == 1: # 홀수
    print(lis[len(lis)//2] ** 2)
else:
    print(lis[len(lis)//2 - 1] * lis[len(lis)//2])