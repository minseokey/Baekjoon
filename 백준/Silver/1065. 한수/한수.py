n = int(input())
lis = []
num = 0
for i in range(1, n+1):
    lis.append(str(i))
for k in range(1, n+1):
    if k < 100:
        num = num + 1
    elif 100 <= k < 1000:
        inslis = []
        for j in range(0, 3):
            stra = lis[k-1]
            inslis.append(int(stra[j]))
        if (inslis[0]-inslis[1]) == (inslis[1]-inslis[2]) and (inslis[0]-inslis[1]) == ((inslis[0]-inslis[2])/2):
            num = num + 1


print(num)