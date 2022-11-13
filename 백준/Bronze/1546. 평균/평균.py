n = int(input())
lis = input().split()
num = 0
numk = 0
for i in range(0, n):
    numk = numk + int(lis[i])
    if int(lis[i]) > num:
        num = int(lis[i])
print((numk / num)*(100 / n))
