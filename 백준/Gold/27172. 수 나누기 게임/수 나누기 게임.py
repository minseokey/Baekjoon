import sys

n = int(input())
lis = list(map(int,sys.stdin.readline().split()))

alllis = [False] * 1000001
llis = [0] * 1000001

for ind,i in enumerate(lis):
    alllis[i] = True



for i in sorted(lis):
    for j in range(i*2 ,1000001,i):
        if alllis[j]:
            llis[j]-=1
            llis[i]+=1

for i in lis:
    print(llis[i],end = " ")
