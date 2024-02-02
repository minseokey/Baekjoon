import sys

n,m = map(int,sys.stdin.readline().split())

string = ""
cand = [str(i+1) for i in range(n)]

def back(now):
    if len(now) == m:
        print(" ".join(now))

    else:
        for i in range(len(cand)):
            if cand[i] not in now:
                now.append(cand[i])
                back(now)
                now.pop()

back([])