import math
import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

ans = 0

key = False


def recur(k):
    global key
    global ans

    if k == s:
        ans = 1
        key = True
        return

    elif len(k) <= len(s):
        return

    else:
        if key:
            return

        if k[0] == "B" and k[-1] == "A":
            recur(k[:-1])
            recur(k[1:][::-1])
        elif k[0] == "B":
            recur(k[1:][::-1])
        elif k[-1] == "A":
            recur(k[:-1])


recur(t)
print(ans)
