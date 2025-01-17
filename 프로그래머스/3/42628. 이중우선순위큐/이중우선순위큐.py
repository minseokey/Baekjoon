from collections import deque
import bisect

def solution(operations):
    answer = deque()
    
    for i in operations:
        order, num = i.split()
        num = int(num)
        if order == "I":
            ind = bisect.bisect_left(answer, num)
            answer.insert(ind, num)
        elif num == 1 and answer:
            answer.pop()
        elif answer:
            answer.popleft()
            
    if answer:
        return [answer[-1], answer[0]]
    else:
        return [0,0]