n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))
for i in range(n):
    print(sorted(lis)[i])