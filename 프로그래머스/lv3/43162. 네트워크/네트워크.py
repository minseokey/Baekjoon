from collections import Counter


def solution(n, computers):

    lis = [i for i in range(n)]

    def union(lis,a,b):
        a = find(lis,a)
        b = find(lis,b)
        if a <= b:
            lis[b] = lis[a]
        else:
            lis[a] = lis[b]

    def find(lis,num):
        if num == lis[num]:
            return num
        return find(lis,lis[num])

    def test(lis,a,b):
        if find(lis,a) == find(lis,b):
            return True
        else:
            return False

    newcom = []
    for i in range(n):
        subcom = []
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                subcom.append(j)
        newcom.append(subcom)

    link = []
    for i in range(len(newcom)):
        for j in newcom[i]:
            if [i, j] not in link and [j, i] not in link:

                link.append([i, j])

    if not link:
        return n

    for i in link:
        union(lis, i[0], i[1])

    for i in range(len(lis)):
        lis[i] = find(lis,lis[i])

    return len(Counter(lis))