n = int(input())
lis = input().split()
a = 0
for i in range(0, n):
    lis[i] = int(lis[i])
    b = 0
    for j in range(1,lis[i] + 1):
        if lis[i] % j == 0:
            b = b + 1
    if b == 2:
        a = a + 1
print(a)