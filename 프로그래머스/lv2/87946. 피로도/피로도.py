import copy

defa = 0
def recur(k, dungeons, count):
    global defa
    for i in dungeons:
        if k >= i[0]:
            copyden = copy.deepcopy(dungeons)
            copyden.remove(i)
            recur(k - i[1], copyden, count + 1)
    defa = max(defa, count)


def solution(k, dungeons):
    global defa
    recur(k,dungeons,0)
    return defa