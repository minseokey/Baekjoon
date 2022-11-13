import copy
import sys,itertools
sys.setrecursionlimit(100000)
targetstr = sys.stdin.readline()
target = int(targetstr)
nobutton = sys.stdin.readline()
num = ['0','1','2','3','4','5','6','7','8','9']
caselist = []
if nobutton != 0:
    wronglis = sys.stdin.readline().split()
    for i in list(wronglis):
        num.remove(i)

caselist.append(abs(100 - target))

temp1= copy.deepcopy(target)
temp2= copy.deepcopy(target)
counter2 = 0
counter1 = 0
while True:
    if counter1 > caselist[0] or temp1 < 0:
        break
    else:
        for i in str(temp1):
            if i not in num:
                temp1 -= 1
                counter1 += 1
                break
        else:
            caselist.append(abs(temp1 - target)+len(str(temp1)))
            break
while True:
    if counter2 > caselist[0]:
        break
    else:
        for i in str(temp2):
            if i not in num:

                temp2 += 1
                counter2 += 1
                break

        else:
            caselist.append(abs(temp2 - target)+len(str(temp2)))
            break


print(min(caselist))