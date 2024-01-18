def solution(edges):
    edgedict = dict()

    # 0번쩨 -> 나가는거, 1번쩨 -> 들어오는거
    for i in edges:
        if i[0] not in edgedict.keys():
            edgedict[i[0]] = [[i[1]], []]
        else:
            edgedict[i[0]][0].append(i[1])
        if i[1] not in edgedict.keys():
            edgedict[i[1]] = [[], [i[0]]]
        else:
            edgedict[i[1]][1].append(i[0])


    middle = -1
    # 중점찾기
    for i in edgedict.keys():
        if len(edgedict[i][0]) >= 2 and not edgedict[i][1]:
            middle = i

    answer = [middle,0,0,0]

    for i in edgedict[middle][0]:
        dfs = [i]
        while dfs:
            now = dfs.pop()
            if not edgedict[now][0]:
                answer[2] += 1
                break

            breakey = False
            for j in edgedict[now][0]:
                if len(edgedict[j][0]) >= 2 and len(edgedict[j][1]) >= 2:
                    breakey = True
                    answer[3] += 1
                elif j == i:
                    breakey = True
                    answer[1] += 1
                    break
                else:
                    dfs.append(j)
            if breakey:
                break

    return answer