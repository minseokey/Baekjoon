import sys

num, need = map(int, sys.stdin.readline().split())
sum = 0
lanlist = [0] * num
tempp = 0
for i in range(num):
    temp = int(sys.stdin.readline())
    lanlist[i] = temp
    sum += temp


best = int(sum / need)
if int(sum / (need + num)) == 0:
    worst = 1
else:
    worst = int(sum / (need + num))


while True:
    mid = int((best + worst) / 2)
    midplus = mid + 1
    midsum = 0
    midplussum = 0

    for i in lanlist:
        midsum += int(i / mid)
        midplussum += int(i / midplus)

    if midsum >= need > midplussum and midsum > midplussum:
        print(mid)
        break
    elif midsum < need:
        best = mid
    elif midsum >= need:
        if best - worst == 1:
            worst += 1
        else:
            worst = mid