import sys,math
n,r,c = map(int,sys.stdin.readline().split())

# N 별로 각각 어디 위치하는지를 구해서 더해가야겠네 ㅋㅋ

positionList = []
scale = 2**n
ans = 0

def findingPosition (r,c,scale):
    global ans
    if scale == 1:
        return
    elif r >= scale/2 and c >= scale/2:
        ans += 3 * ((scale/2)**2)
        findingPosition(r - scale/2,c - scale/2 , scale/2)
    elif r >= scale/2 :
        ans += 2 * ((scale/2) **2)
        findingPosition(r - scale / 2, c, scale / 2)
    elif c >= scale/2 :
        ans += 1 * ((scale/2) **2)
        findingPosition(r, c - scale / 2, scale / 2)
    else:
        findingPosition(r, c, scale / 2)


findingPosition(r,c,scale)
print(int(ans))

