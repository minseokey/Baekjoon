import copy
import sys

n = int(sys.stdin.readline())
lis = list(sys.stdin.readline().strip())
goal = list(sys.stdin.readline().strip())


for i in range(n):
    lis[i] = int(lis[i])
    goal[i] = int(goal[i])

queue = [(lis, 0)]

for i in range(n):
    newqueue = []
    while queue:
        temp,num = queue.pop()
        if i == 0:
            newtemp = copy.deepcopy(temp)
            newtemp[0] = abs(newtemp[0] - 1)
            newtemp[1] = abs(newtemp[1] - 1)
            newqueue.append((newtemp,1))
            newqueue.append((temp,0))

        elif 0 < i < n-1:
            if temp[i-1] == goal[i-1]:
                newqueue.append((temp,num))
            else:
                temp[i-1] = abs(temp[i-1] - 1)
                temp[i] = abs(temp[i] - 1)
                temp[i+1] = abs(temp[i+1] - 1)
                newqueue.append((temp,num+1))
        else:
            if temp[i-1] == goal[i-1] and temp[i] == goal[i]:
                newqueue.append((temp,num))
            elif temp[i-1] != goal[i-1] and temp[i] != goal[i]:
                temp[i-1] = abs(temp[i-1] - 1)
                temp[i] = abs(temp[i] - 1)
                newqueue.append((temp,num+1))

    queue = newqueue

if queue:
    print(queue[0][1])
else:
    print(-1)