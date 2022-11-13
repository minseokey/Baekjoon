firL = []
ansL = []
insnum = 0
for i in range(1, 10001):
    ansL.append(i)
    numstr = str(i)
    insnum = i
    for k in range(0,len(numstr)):
        insnum = int(numstr[k]) + insnum
    firL.append(insnum)

for j in range(0,len(firL)):
    if firL[j] in ansL:
        ansL.remove(firL[j])

for k in range(0,len(ansL)):
    print(ansL[k])