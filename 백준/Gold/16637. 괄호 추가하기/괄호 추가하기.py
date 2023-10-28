import copy
import itertools
import sys
from collections import deque

n = int(sys.stdin.readline())
lis = sys.stdin.readline().strip()
maxx = -float('inf')

sim = []
num = []

for i in lis:
    if i in ["+", "-", "*"]:
        sim.append(i)
    else:
        num.append(int(i))
leng = len(sim) - 1

# 0,1 계산 -> 0번째 기호
# 0,2,4.... or 0,2,5 처럼 괄호는 중간 하나를 꼭 띄워야함.
allis = []


def dfs(l, now):
    global leng
    if now > leng:
        allis.append(copy.deepcopy(l))
    elif not l:
        l.append(now)
        dfs(l, now + 1)
        l.pop()
        dfs(l, now + 1)
    else:
        if l[-1] + 1 < now:
            l.append(now)
            dfs(l, now + 1)
            l.pop()
            dfs(l, now + 1)
        else:
            dfs(l, now + 1)


dfs([], 0)


def calc(prime, cnum, csim):
    global maxx
    for k in prime:
        tsim = csim.pop(k)
        tn1 = cnum.pop(k)
        tn2 = cnum.pop(k)
        if tsim == "+":
            cnum.insert(k, tn1 + tn2)
        elif tsim == "*":
            cnum.insert(k, tn1 * tn2)
        else:
            cnum.insert(k, tn1 - tn2)

    while csim:
        tsim = csim.pop(0)
        tn1 = cnum.pop(0)
        tn2 = cnum.pop(0)
        if tsim == "+":
            cnum.insert(0, tn1 + tn2)
        elif tsim == "*":
            cnum.insert(0, tn1 * tn2)
        else:
            cnum.insert(0, tn1 - tn2)

    if maxx <= cnum[0]:
        maxx = cnum[0]


for i in allis:
    for j in range(len(i)):
        i[j] -= j
    calc(i, copy.deepcopy(num), copy.deepcopy(sim))

print(maxx)
