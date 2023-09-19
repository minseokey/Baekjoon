import sys

n,l = map(int,sys.stdin.readline().split())

lis = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

able = 0
okroad = [False] * n
garo = [[False] * n for _ in range(n)]
# 가로
for i in range(n):
    # 정방으로 갈때 문제가 없는가
    fstack = []
    key = True
    for j in range(n):
        if not fstack:
            fstack.append([j,lis[i][j]])
        elif fstack[-1][1] == lis[i][j]:
            fstack.append([j,lis[i][j]])
        elif fstack[-1][1]+1 == lis[i][j]:
            if len(fstack) >= l:
                for k in range(l):
                    temp = fstack.pop()
                    if garo[i][temp[0]]:
                        key = False
                        break
                    else:
                        garo[i][temp[0]] = True
                if not key:
                    break
                fstack.clear()
                fstack.append([j,lis[i][j]])
            else:
                key = False
                break
        elif fstack[-1][1] == lis[i][j] + 1:
            fstack.clear()
            fstack.append([j,lis[i][j]])
        else:
            key = False
            break
    if key:
        okroad[i] = True

    # 역방으로 갈때는 문제가 없는가
    bstack = []
    key = True
    for j in range(n-1,-1,-1):
        if not bstack:
            bstack.append([j,lis[i][j]])
        elif bstack[-1][1] == lis[i][j]:
            bstack.append([j,lis[i][j]])
        elif bstack[-1][1]+1 == lis[i][j]:
            if len(bstack) >= l:
                for k in range(l):
                    temp = bstack.pop()
                    if garo[i][temp[0]]:
                        key = False
                        break
                    else:
                        garo[i][temp[0]] = True
                if not key:
                    break
                bstack.clear()
                bstack.append([j,lis[i][j]])
            else:
                key = False
                break
        elif bstack[-1][1] == lis[i][j] + 1:
            bstack.clear()
            bstack.append([j,lis[i][j]])
        else:
            key = False
            break
    if key:
        if okroad[i]:
            able += 1


sero = [[False] * n for _ in range(n)]
okroad = [False] * n
# 세로
for j in range(n):
    # 정방으로 갈때 문제가 없는가
    fstack = []
    key = True
    for i in range(n):
        if not fstack:
            fstack.append([i,lis[i][j]])
        elif fstack[-1][1] == lis[i][j]:
            fstack.append([i,lis[i][j]])
        elif fstack[-1][1]+1 == lis[i][j]:
            if len(fstack) >= l:
                for k in range(l):
                    temp = fstack.pop()
                    if sero[temp[0]][j]:
                        key = False
                        break
                    else:
                        sero[temp[0]][j] = True
                if not key:
                    break
                fstack.clear()
                fstack.append([i,lis[i][j]])
            else:
                key = False
                break
        elif fstack[-1][1] == lis[i][j] + 1:
            fstack.clear()
            fstack.append([i,lis[i][j]])
        else:
            key = False
            break
    if key:
        okroad[j] = True
    # 역방으로 갈때는 문제가 없는가
    bstack = []
    key = True
    for i in range(n - 1, -1, -1):
        if not bstack:
            bstack.append([i,lis[i][j]])
        elif bstack[-1][1] == lis[i][j]:
            bstack.append([i,lis[i][j]])
        elif bstack[-1][1]+1 == lis[i][j]:
            if len(bstack) >= l:
                for k in range(l):
                    temp = bstack.pop()
                    if sero[temp[0]][j]:
                        key = False
                        break
                    else:
                        sero[temp[0]][j] = True
                if not key:
                    break
                bstack.clear()
                bstack.append([i,lis[i][j]])
            else:
                key = False
                break
        elif bstack[-1][1] == lis[i][j] + 1:
            bstack.clear()
            bstack.append([i,lis[i][j]])
        else:
            key = False
            break
    if key:
        if okroad[j]:
            able += 1

print(able)
