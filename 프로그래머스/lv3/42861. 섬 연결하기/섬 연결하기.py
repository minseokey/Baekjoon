def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    checklist = [i for i in range(n)]


    print(costs)
    #맨위의 부모 찾기
    def getParents(lis,num):
        if lis[num] == num:
            return num
        return getParents(lis,lis[num])

    ## 두 노드의 부모 비교
    def findParents(lis,numa,numb):
        a = getParents(lis,numa)
        b = getParents(lis,numb)
        if a == b:
            return True
        else:
            return False

    ##각 부모의 노드를 합침
    def unionParent(lis,numa,numb):
        a = getParents(lis,numa)
        b = getParents(lis,numb)
        if a < b:
            lis[b] = a
        else:
            lis[a] = b


    summ = 0
    for n1, n2, cost in costs:
        if getParents(checklist,n1) != getParents(checklist,n2):
            unionParent(checklist,n1, n2)
            summ += cost

    return summ
