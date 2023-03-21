import sys

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
lisalready = [[lis[i]] for i in range(len(lis))]

for i in range(1, len(lis)):
    nowlis = []
    for j in range(0, i):
        if lis[j] < lis[i]:
            nowlis = max(lisalready[j], nowlis, key=lambda x: len(x))

    lisalready[i] = nowlis + lisalready[i]

print(len(max(lisalready,key=lambda x: len(x))))
print(*max(lisalready,key=lambda x: len(x)))
