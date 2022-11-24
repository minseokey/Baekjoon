def solution(sizes):
    amax = 0
    bmax = 0
    for i in sizes:
        a = max(i)
        if a > amax:
            amax = a
        b = min(i)
        if b > bmax:
            bmax = b


    return amax*bmax
