import heapq
def solution(jobs):
    answer = dict()
    for i in jobs:
        if i[0] not in answer.keys():
            answer.update({i[0]:[(i[1],i[0])]})
        else:
            answer[i[0]].append((i[1],i[0]))

    heapA = []
    count = 0
    beforeCpu = 0
    cputime = 0
    while answer or heapA:
        for i in range(beforeCpu,cputime + 1):
            if i in answer.keys():
                for j in answer[i]:
                    heapq.heappush(heapA,j)
                del(answer[i])
        if heapA:
            beforeCpu = cputime
            temp = heapq.heappop(heapA)
            # print(temp[0] - temp[1] + cputime,cputime,temp)
            count += temp[0] - temp[1] + cputime
            cputime += temp[0]
        else:
            beforeCpu = cputime
            cputime += 1

        # print(count)

    return int((count)/len(jobs))
