import sys


def solution(n, times):
    mintime = times[0]
    maxtime = sys.maxsize

    before = 0
    while True:
        now = (mintime+maxtime)//2
        count = 0
        for i in times:
            count += now // i
        print(now,before)
        if count < n:
            if before == now+1:
                return before
            else:
                mintime = (maxtime+mintime) // 2 - 1
        else:
            if count < n:
                mintime = (maxtime + mintime) // 2 - 1
            else:
                maxtime = (mintime + maxtime) // 2 + 1

        before = now + 1