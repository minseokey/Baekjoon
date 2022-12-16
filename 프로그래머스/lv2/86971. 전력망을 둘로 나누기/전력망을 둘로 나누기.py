#  전체 순환, 하나씩 연결을 제외
# 이랬을때 가장 작은 값을 구하면 듯?
import copy

count = 1
def dfs(dic,already,start):
    global count
    if start in dic.keys():
        for i in dic[start]:
            if i not in already:
                already.append(i)
                count += 1
                dfs(dic,already,i)

def cluster(n,exc,wires):
    global count
    count = 1
    wires = copy.deepcopy(wires)
    wires.remove(exc)
    nodedic = dict()
    for i in wires:
        if i[0] in nodedic.keys():
            nodedic[i[0]].append(i[1])
        else:
            nodedic[i[0]] = [i[1]]

        if i[1] in nodedic.keys():
            nodedic[i[1]].append(i[0])
        else:
            nodedic[i[1]] = [i[0]]

    dfs(nodedic,[1],1)
    return abs(n - count*2)


def solution(n, wires):
    lis = []
    for i in wires:
        lis.append(cluster(n,i,wires))
    return min(lis)