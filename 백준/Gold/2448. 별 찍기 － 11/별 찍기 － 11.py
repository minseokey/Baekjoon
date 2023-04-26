import math

n = int(input())

lis = [[" "," ","*"," "," "],
       [" ","*"," ","*"," "],
       ["*","*","*","*","*"]]

def recur(size):
    tempsize = 3*(2**(size))
    tempdef = [[" " for i in range(2 * tempsize - 1)] for j in range(tempsize)]

    for i in range(len(lis)):
        for j in range(len(lis[i])):
        # 상
            tempdef[i][j+tempsize//2] = lis[i][j]
        # 좌하
            tempdef[i + (tempsize//2)][j] = lis[i][j]
        # 우하
            tempdef[i + (tempsize//2)][j+tempsize] = lis[i][j]

    return tempdef

for i in range(1,int(math.log(n//3,2)) + 1):
    lis = recur(i)

for i in lis:
    print("".join(i))
