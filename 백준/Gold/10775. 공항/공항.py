import bisect
import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())

alllis = [[i,False] for i in range(g + 1)]

count = 0
for i in range(p):
    tp = int(sys.stdin.readline())
    ind = bisect.bisect_left(alllis,tp,key=lambda x : x[0])
    key = False
    while ind > 0:
        if not alllis[ind][1]:
            alllis[ind][0] = tp
            alllis[ind][1] = True
            key = True
            break
        else:
            ind -= 1

    if key:
        count += 1
    else:
        break


print(count)