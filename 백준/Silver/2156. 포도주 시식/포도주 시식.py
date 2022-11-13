
n = int(input())
lis = [int(input()) for i in range(n)]
lisadd = [[0,0,0] for j in range(n + 1)] # 0번째 = 다음꺼 o ,1번째 = 다음꺼 x ,2번째 = 다음꺼 o 두칸뛰어서
maxx = 0
if n == 1:
    print(lis[0])
else:
    lisadd[1][0],lisadd[1][1],lisadd[2][0],lisadd[2][1],lisadd[1][2],lisadd[2][2] = 0,lis[0],lis[1],lis[0]+lis[1],0,0
    for i in range(2,len(lis)):
        lisadd[i + 1][0] = max(lisadd[i - 1]) + lis[i]
        lisadd[i + 1][1] = max(lisadd[i][0],lisadd[i][2]) + lis[i]
        lisadd[i + 1][2] = max(lisadd[i - 2]) + lis[i]

    for i in range(n):
        for j in range(2):
            if maxx < lisadd[i+1][j]:
                maxx = lisadd[i+1][j]

    else:
        print(maxx)
