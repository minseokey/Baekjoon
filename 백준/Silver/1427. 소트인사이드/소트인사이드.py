a = input()
lis = []
for i in range(len(a)):
    lis.append(int(a[i]))
k = list(reversed(sorted(lis)))
for i in k:
    print(i,end = "")