def solution(n, lost, reserve):
    setlost = list(set(lost) - set(reserve))
    setreserve = list(set(reserve) - set(lost))
    for i in range(len(setlost)):
        if setlost[i] -1 in setreserve:
            setreserve.remove(setlost[i]-1)
        elif setlost[i] + 1 in setreserve:
            setreserve.remove(setlost[i]+1)
            
    return n - (len(lost) - (len(reserve) - len(setreserve)))