foi = int(input())
numins = 0
numtot = 0
for i in range(0, foi):
    lissep = []
    lis = input()
    numins = 0
    numtot = 0
    for k in range(0, len(lis)):
        lissep.append(lis[k])
    for j in range(0, len(lissep)):
        if lissep[j] == "X":
            numins = 0
        elif lissep[j] == "O":
            numins = numins + 1
            numtot = numtot + numins
    print(numtot)
    