import copy
import heapq
import collections
def solution(priorities, location):
    heappri = copy.copy([-i for i in priorities])
    heapq.heapify(heappri)

    stackk = collections.deque()
    for i in range(len(priorities)):
        stackk.append([priorities[i],i])

    find = True
    tempmax = 0
    count = 1
    while True:
        if find:
            tempmax = -heapq.heappop(heappri)
            find = False
        temp = stackk.popleft()

        if temp[0] == tempmax:
            if temp[1] == location:
                break
            else:
                count += 1
                find = True
        else:
            stackk.append(temp)


    return count