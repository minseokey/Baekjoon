H,M = map(int,input().split())

if (M >= 45):
    NewM = (M - 45)
    NewH = H
    print(NewH , NewM)
elif (M < 45) and (H > 0):
    NewM = (M + 15)
    NewH = (H - 1)
    print(NewH , NewM)
elif (M < 45) and (H == 0):
    NewM = (M + 15)
    NewH = 23
    print(NewH , NewM)