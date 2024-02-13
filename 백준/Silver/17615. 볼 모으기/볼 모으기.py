import sys

n = int(sys.stdin.readline())
lis = list(sys.stdin.readline())

tempR = 0 # 빨강 옴기기
tempB = 0 # 파랑 옴기기

Rkey = False
Bkey = False
while n >= 0:
    if lis[n] == "R" and Rkey:
        tempR += 1
    if lis[n] == "B" and not Rkey:
        Rkey = True
    if lis[n] == "B" and Bkey:
        tempB += 1
    if lis[n] == "R" and not Bkey:
        Bkey = True
    n -= 1
print(min(tempR,tempB))


