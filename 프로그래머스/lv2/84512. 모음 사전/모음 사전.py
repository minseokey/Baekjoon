import itertools
def solution(word):
    dic = []
    dicc = []
    lis = ["A","E","I","O","U"]
    for i in range(1,6):
        dic += list(itertools.product(lis,repeat = i))
    for i in dic:
        dicc.append("".join([*i]))
    dicc.sort()
    print(dicc)
    return dicc.index(word) + 1