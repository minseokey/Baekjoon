import sys
num = int(sys.stdin.readline())
lis = []
for i in range(num):
    k = list(map(int,sys.stdin.readline().split()))
    lis.append(k)

bluecount = 0
whitecount = 0
def recur(x,y,length):
    global bluecount,whitecount
    starter = lis[y][x]
    key = True
    for i in range(x,x+length):
        for j in range(y,y+length):
            if lis[j][i] != starter:
                key = False
                break
    if key == True:
        if starter == 1:
            bluecount += 1
        else:
            whitecount += 1
        return
    else:
        recur(x+int(length / 2), y, int(length / 2))
        recur(x, y+int(length / 2), int(length / 2))
        recur(x, y, int(length / 2))
        recur(x+int(length / 2), y+int(length / 2), int(length / 2))

recur(0,0,num)

print(whitecount)
print(bluecount)