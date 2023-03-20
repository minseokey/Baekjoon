import sys

n,m = map(int,sys.stdin.readline().split())

big,smal = 1,1
for i in range(m):
    big *= n
    n-=1
    smal *= m
    m -=1

print(big//smal)