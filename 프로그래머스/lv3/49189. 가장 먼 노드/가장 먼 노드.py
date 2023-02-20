def solution(n, edge):
    a = {}
    for i in edge:
        if i[0] -1 in a.keys():
            a[i[0] -1].append(i[1] -1)
        else:
            a[i[0] -1] = [i[1] -1]

        if i[1] -1 in a.keys():
            a[i[1] -1].append(i[0] -1)
        else:
            a[i[1] -1] = [i[0] -1]


    lis = [False for i in range(n)]
    lis[0] = True
    t = [0]
    while t:
        temp = []
        for i in t:
            for j in a[i]:
                if j in a.keys() and not lis[j]:
                    temp.append(j)
                    lis[j] = True
        if not temp:
            return len(t)
        t = temp
