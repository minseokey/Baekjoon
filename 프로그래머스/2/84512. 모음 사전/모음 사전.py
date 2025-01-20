import itertools

def solution(word):
    tmp = []
    for i in range(6):
        tmp += itertools.product(["A","E","I","O","U"], repeat = i)
    tmp.sort()
    return tmp.index(tuple(word))
