import sys

n = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))
lis.sort()

ans = [[],float('inf')]
for i in range(len(lis) - 2):
    base = lis[i]
    # 투포인터
    start = i+1
    end = len(lis) - 1
    tempans = ans[1]
    key = False
    while start < end:
        temp = lis[start] + lis[end] + base

        if tempans > abs(temp):
            tempans = abs(temp)
            ans = [[base,lis[start],lis[end]],tempans]

        if temp > 0:
            end -= 1
        else:
            start += 1

print(*ans[0])