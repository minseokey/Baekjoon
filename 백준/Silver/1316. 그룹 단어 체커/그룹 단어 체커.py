n = int(input())
ans = 0
for o in range(0,n):
    wor = str(input())
    lis = []
    for j in range(0,len(wor)):
        lis.append(wor[j])
    for i in range(0,len(lis)-1):
        if lis[i] == lis[i+1]:
            lis[i] = ("{}".format(i))
    alplis = []
    for i in range(0,len(lis)):
        if not lis[i] in alplis:
            alplis.append(lis[i])
        elif lis[i] in alplis:
            ans = ans + 1
            break

print(n - ans)