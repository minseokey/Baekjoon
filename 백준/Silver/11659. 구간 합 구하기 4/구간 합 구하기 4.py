import sys
num,fois = map(int,sys.stdin.readline().split())
lis = [0] * (num + 1)
orilis = list(map(int,sys.stdin.readline().split()))
for i in range(len(lis) - 1):
    lis[i+1] = orilis[i]+ lis[i]

for i in range(fois):
    st , en = map(int,sys.stdin.readline().split())
    print(lis[en] - lis[st - 1])
