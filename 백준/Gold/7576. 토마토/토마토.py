import sys
import collections

m,n = map(int,sys.stdin.readline().split())
box = []
for i in range(n):
    box.append(list(map(int,sys.stdin.readline().split())))

checkedList = [[False for i in range(m)] for j in range(n)]
checkedDeque = collections.deque()

def Checker(ripeTo):
    x,y,z = ripeTo[0],ripeTo[1],ripeTo[2]
    if x < n-1 and box[x + 1][y] == 0 and not checkedList[x + 1][y]:
        checkedDeque.append((x+1,y,z+1))
        checkedList[x+1][y] = True
        box[x+1][y] = 1
    if x > 0 and box[x - 1][y] == 0 and not checkedList[x - 1][y]:
        checkedDeque.append((x-1,y,z+1))
        checkedList[x-1][y] = True
        box[x - 1][y] = 1
    if y < m-1 and box[x][y + 1] == 0 and not checkedList[x][y + 1]:
        checkedDeque.append((x,y+1,z+1))
        checkedList[x][y+1] = True
        box[x][y+1] = 1
    if y > 0 and box[x][y - 1] == 0 and not checkedList[x][y - 1]:
        checkedDeque.append((x,y-1,z+1))
        checkedList[x][y-1] = True
        box[x][y-1] = 1


for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            checkedDeque.append((i,j,0))

maxx = 0
while checkedDeque:
    temp = checkedDeque.popleft()
    if temp[2] > maxx:
        maxx = temp[2]
    Checker(temp)

checker = True
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            checker = False
            break
    if not checker:
        break

if checker:
    print(maxx)
else:
    print(-1)
