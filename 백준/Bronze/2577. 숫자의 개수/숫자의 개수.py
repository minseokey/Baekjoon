firn = int(input())
secn = int(input())
tirn = int(input())
Num = str(firn * secn * tirn)
NumL = []
alpha = []
t = 0
for h in range(0, (len(Num))):
    NumL.append(int(Num[h]))
for i in range(0,10):
    for j in range(0, len(NumL)):
        if i == NumL[j]:
            t = t+1
    alpha.append(t)
    t = 0

for k in range(0, len(alpha)):
    print(alpha[k])
