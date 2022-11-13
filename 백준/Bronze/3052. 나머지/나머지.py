lis = []
LisL = []
while True:
    try:
        Num = int(input())
        goal = Num % 42
        lis.append(goal)
    except:
        break

for i in range(0, len(lis)):
    if not lis[i] in LisL:
        LisL.append(lis[i])
print(len(LisL))

    