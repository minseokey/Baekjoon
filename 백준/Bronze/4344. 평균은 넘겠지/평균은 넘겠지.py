foi = int(input())
for i in range(0,foi):
    lis = input().split()
    n = int(lis[0])
    lis.pop(0)
    newlis = []
    summ = 0
    a = 0
    b = 0
    for k in range(0,len(lis)):
        newlis.append(int(lis[k]))
        summ = summ + int(lis[k])
    ave = summ/n
    for j in range(0,len(newlis)):
        if newlis[j] > ave:
            a = a + 1
    print("%.3f%s"%(a/n*100,"%"))
