import copy
import itertools
import sys

n, m, k = map(int, sys.stdin.readline().split())
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
spin = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

random = itertools.permutations(spin, len(spin))
mini = float("inf")


def spin(templis, lefthigh, rightlow):
    top = lefthigh[0]
    left = lefthigh[1]
    bottom = rightlow[0]
    right = rightlow[1]
    while bottom - top > 1 and right - left > 1:
        # 세로축부터 이동.
        rightext ,lefttext = 0,0
        for i in range(top,bottom + 1):
            t = templis[i][right]
            templis[i][right] = rightext
            rightext = t
        for i in range(bottom, top-1, -1):
            t = templis[i][left]
            templis[i][left] = lefttext
            lefttext = t

        # 지금 남은 topext, botext 는 끼워넣을 숫자
        for i in range(left + 1, right + 1):
            t = templis[top][i]
            templis[top][i] = lefttext
            lefttext = t
        for i in range(right - 1, left - 1, -1):
            t = templis[bottom][i]
            templis[bottom][i] = rightext
            rightext = t

        right -= 1
        bottom -= 1
        left += 1
        top += 1
def minimum(templis):
    tempmin = float("inf")
    for i in templis:
        if tempmin >= sum(i):
            tempmin = sum(i)
    return tempmin


for temp in random:
    templis = copy.deepcopy(lis)
    for jr, jc, js in temp:
        lefthigh = [jr - js - 1, jc - js - 1]
        rightlow = [jr + js - 1, jc + js - 1]
        spin(templis, lefthigh, rightlow)

    mini = min(mini, minimum(templis))
print(mini)
