num = int(input())
lis = [0]*(num+1)
lis[0] = 1
lis[1] = 2
if num == 1:
    print(1)
else:
    for i in range(2, num+1):
        lis[i] = (lis[i-1] + lis[i-2])%10007
    print(lis[num - 1])
