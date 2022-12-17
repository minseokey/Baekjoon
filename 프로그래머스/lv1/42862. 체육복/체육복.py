import copy


lis = []
def recur(reserve, lostindex, lost, count):

    if lostindex == len(lost):
        lis.append(count)
        return

    if lost[lostindex] in reserve:
        newreserve1 = copy.deepcopy(reserve)
        newreserve1.remove(lost[lostindex])
        recur(newreserve1,lostindex + 1,lost,count+1)
    if lost[lostindex]-1 in reserve:
        newreserve2 = copy.deepcopy(reserve)
        newreserve2.remove(lost[lostindex] - 1)
        recur(newreserve2,lostindex + 1,lost,count+1)
    if lost[lostindex]+1 in reserve:
        newreserve3 = copy.deepcopy(reserve)
        newreserve3.remove(lost[lostindex] + 1)
        recur(newreserve3,lostindex + 1,lost,count+1)
    else:
        recur(reserve,lostindex+1,lost,count)

def solution(n, lost, reserve):

    recur(reserve,0,lost,0)
    return n - (len(lost) - max(lis))