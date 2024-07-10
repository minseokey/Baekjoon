import sys

p, m = map(int,sys.stdin.readline().split())
roomlist = []
started = set()

for _ in range(p):
    lev, nick = map(str, sys.stdin.readline().split())
    lev = int(lev)

    joined = False
    for i in range(len(roomlist)):
        # 시작하지 않고
        if i not in started:
            # 레벨이 처음 입장한놈 기준으로 +- 10 인지
            if roomlist[i][0][0]-10 <= lev <= roomlist[i][0][0]+10:
                roomlist[i].append((lev, nick))
                joined = True
                if len(roomlist[i]) == m:
                    started.add(i)
        if joined:
            break

    if not joined:
        roomlist.append([(lev, nick)])
        if m == 1:
            started.add(len(roomlist) - 1)

for i in range(len(roomlist)):
    if i in started:
        print("Started!")
    else:
        print("Waiting!")
    roomlist[i].sort(key= lambda x:x[1])
    for j in roomlist[i]:
        print(j[0], j[1])