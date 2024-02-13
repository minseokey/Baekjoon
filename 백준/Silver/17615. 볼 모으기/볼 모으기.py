import sys

n = int(sys.stdin.readline())
lis = list(sys.stdin.readline())

tempR = 0
tempB = 0
Rkey = False
Bkey = False

for i in lis[::-1]:
    if i == "R":
        if Rkey:
            tempR += 1
        if not Bkey:
            Bkey = True
    if i == "B":
        if Bkey:
            tempB += 1
        if not Rkey:
            Rkey = True

tempR_1 = 0
tempB_1 = 0
Rkey = False
Bkey = False

for i in lis:
    if i == "R":
        if Rkey:
            tempR_1 += 1
        if not Bkey:
            Bkey = True
    if i == "B":
        if Bkey:
            tempB_1 += 1
        if not Rkey:
            Rkey = True

print(min(tempR, tempB, tempR_1, tempB_1))
