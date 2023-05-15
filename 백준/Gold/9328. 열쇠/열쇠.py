import sys
from collections import deque

fois = int(sys.stdin.readline().strip())
for _ in range(fois):
    y, x = map(int, sys.stdin.readline().split())
    lis = [list(sys.stdin.readline().strip()) for i in range(y)]
    keypurse = list(sys.stdin.readline().strip())
    if keypurse == ['0']:
        keypurse = []
    visited = [[False for i in range(x)] for j in range(y)]
    lockeddoor = dict()


    # 가장자리 벽이아닌 위치 파악
    def enter():
        k = 0
        enterlist = deque()
        for i in range(x):
            if lis[0][i] == ".":
                enterlist.append([0, i])
                visited[0][i] = True
            elif lis[0][i] == "$":
                enterlist.append([0, i])
                visited[0][i] = True
                k += 1
            elif lis[0][i].islower():
                enterlist.append([0, i])
                visited[0][i] = True
                keypurse.append(lis[0][i])
            elif lis[0][i].isupper():
                if lis[0][i].lower() in keypurse:
                    enterlist.append([0, i])
                    visited[0][i] = True
                else:
                    if lis[0][i].lower() not in lockeddoor.keys():
                        lockeddoor[lis[0][i].lower()] = deque()
                    lockeddoor[lis[0][i].lower()].append([0, i])

            if lis[-1][i] == ".":
                enterlist.append([y - 1, i])
                visited[y-1][i] = True
            elif lis[-1][i] == "$":
                enterlist.append([y-1, i])
                visited[y - 1][i] = True
                k += 1
            elif lis[-1][i].islower():
                enterlist.append([y - 1, i])
                visited[y - 1][i] = True
                keypurse.append(lis[-1][i])
            elif lis[-1][i].isupper():
                if lis[-1][i].lower() in keypurse:
                    enterlist.append([y - 1, i])
                    visited[y - 1][i] = True
                else:
                    if lis[-1][i].lower() not in lockeddoor.keys():
                        lockeddoor[lis[-1][i].lower()] = deque()
                    lockeddoor[lis[-1][i].lower()].append([y-1, i])

        for i in range(1,y - 1):
            if lis[i][0] == ".":
                enterlist.append([i, 0])
                visited[i][0] = True
            elif lis[i][0] == "$":
                enterlist.append([i, 0])
                visited[i][0] = True
                k += 1
            elif lis[i][0].islower():
                enterlist.append([i, 0])
                visited[i][0] = True
                keypurse.append(lis[i][0])
            elif lis[i][0].isupper():
                if lis[i][0].lower() in keypurse:
                    enterlist.append([i, 0])
                    visited[i][0] = True
                else:
                    if lis[i][0].lower() not in lockeddoor.keys():
                        lockeddoor[lis[i][0].lower()] = deque()
                    lockeddoor[lis[i][0].lower()].append([i, 0])

            if lis[i][-1] == ".":
                enterlist.append([i, x - 1])
                visited[i][x - 1] = True
            elif lis[i][-1] == "$":
                enterlist.append([i, x-1])
                visited[i][x - 1] = True
                k += 1
            elif lis[i][-1].islower():
                enterlist.append([i, x - 1])
                visited[i][x - 1] = True
                keypurse.append(lis[i][-1])
            elif lis[i][-1].isupper():
                if lis[i][-1].lower() in keypurse:
                    enterlist.append([i, x - 1])
                    visited[i][x - 1] = True
                else:
                    if lis[i][-1].lower() not in lockeddoor.keys():
                        lockeddoor[lis[i][-1].lower()] = deque()
                    lockeddoor[lis[i][-1].lower()].append([i, x-1])

        return [enterlist, k]


    # 모든 경우의수 파악 (BFS), 여기서 열쇠를 주우면 열쇠지갑에 넣기
    queue = deque()
    temp = enter()
    queue += temp[0]
    ans = temp[1]

    testset = set()

    while queue:
        ty, tx = queue.popleft()

        if lis[ty][tx] == '$':
            lis[ty][tx] = '.'
            testset.add((ty,tx))

        if ty < y - 1 and not visited[ty + 1][tx]:
            temp1 = lis[ty + 1][tx]
            if temp1 == ".":
                queue.append([ty + 1, tx])
                visited[ty + 1][tx] = True

            elif temp1 == "$":
                queue.append([ty + 1, tx])
                visited[ty + 1][tx] = True
                ans += 1

            elif temp1.islower():
                keypurse.append(temp1)
                if temp1 in lockeddoor.keys():
                    queue += lockeddoor[temp1]
                    lockeddoor.pop(temp1)
                queue.append([ty + 1, tx])
                visited[ty + 1][tx] = True

            elif temp1.isupper():
                visited[ty + 1][tx] = True
                if temp1.lower() in keypurse:
                    queue.append([ty + 1, tx])
                else:
                    if temp1.lower() not in lockeddoor.keys():
                        lockeddoor[temp1.lower()] = deque()
                    lockeddoor[temp1.lower()].append([ty + 1, tx])

        if ty > 0 and not visited[ty - 1][tx]:
            temp2 = lis[ty - 1][tx]
            if temp2 == ".":
                queue.append([ty - 1, tx])
                visited[ty - 1][tx] = True

            elif temp2 == "$":
                queue.append([ty - 1, tx])
                visited[ty - 1][tx] = True
                ans += 1

            elif temp2.islower():
                keypurse.append(temp2)
                if temp2 in lockeddoor.keys():
                    queue += lockeddoor[temp2]
                    lockeddoor.pop(temp2)
                queue.append([ty - 1, tx])
                visited[ty - 1][tx] = True

            elif temp2.isupper():
                visited[ty - 1][tx] = True
                if temp2.lower() in keypurse:
                    queue.append([ty - 1, tx])
                else:
                    if temp2.lower() not in lockeddoor.keys():
                        lockeddoor[temp2.lower()] = deque()
                    lockeddoor[temp2.lower()].append([ty - 1, tx])

        if tx < x - 1 and not visited[ty][tx + 1]:
            temp3 = lis[ty][tx + 1]
            if temp3 == ".":
                queue.append([ty, tx + 1])
                visited[ty][tx + 1] = True

            elif temp3 == "$":
                queue.append([ty, tx + 1])
                visited[ty][tx + 1] = True
                ans += 1

            elif temp3.islower():
                keypurse.append(temp3)
                if temp3 in lockeddoor.keys():
                    queue += lockeddoor[temp3]
                    lockeddoor.pop(temp3)
                queue.append([ty, tx + 1])
                visited[ty][tx + 1] = True

            elif temp3.isupper():
                visited[ty][tx + 1] = True
                if temp3.lower() in keypurse:
                    queue.append([ty, tx + 1])
                else:
                    if temp3.lower() not in lockeddoor.keys():
                        lockeddoor[temp3.lower()] = deque()
                    lockeddoor[temp3.lower()].append([ty, tx + 1])

        if tx > 0 and not visited[ty][tx - 1]:
            temp4 = lis[ty][tx - 1]
            if temp4 == ".":
                queue.append([ty, tx - 1])
                visited[ty][tx - 1] = True

            elif temp4 == "$":
                queue.append([ty, tx - 1])
                visited[ty][tx - 1] = True
                ans += 1

            elif temp4.islower():
                keypurse.append(temp4)
                if temp4 in lockeddoor.keys():
                    queue += lockeddoor[temp4]
                    lockeddoor.pop(temp4)
                queue.append([ty, tx - 1])
                visited[ty][tx - 1] = True

            elif temp4.isupper():
                visited[ty][tx - 1] = True
                if temp4.lower() in keypurse:
                    queue.append([ty, tx - 1])
                else:
                    if temp4.lower() not in lockeddoor.keys():
                        lockeddoor[temp4.lower()] = deque()
                    lockeddoor[temp4.lower()].append([ty, tx - 1])

    print(ans)
