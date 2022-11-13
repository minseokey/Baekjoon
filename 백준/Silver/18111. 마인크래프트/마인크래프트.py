import sys

y,x,numtile = map(int,sys.stdin.readline().split())

tile = []
for i in range(y):
    tile += list(map(int,sys.stdin.readline().split()))

maxx = max(tile)
minn = min(tile)

abletilelis = []


for i in range(maxx+1 - minn):
    key = True
    timer = 0
    numtemp = numtile
    avglevel = maxx - i

    for j in tile:
        if j == avglevel:
            pass
        elif j > avglevel:
            timer += 2 * (j - avglevel)
            numtemp += (j - avglevel)
        elif j < avglevel:
            timer += (avglevel - j)
            numtemp -= (avglevel - j)

    if numtemp < 0:
        pass
    else:
        abletilelis.append([timer,avglevel])

maxxx = [min(abletilelis)[0],0]

for i in abletilelis:
    if i[0] == min(abletilelis)[0]:
        if i[1] > maxxx[1]:
            maxxx[1] = i[1]

print(maxxx[0],maxxx[1])