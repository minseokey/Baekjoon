import collections
def solution(progresses, speeds):
    a = collections.deque()
    for i in range(len(progresses)):
        a.append([progresses[i],speeds[i]])

    answer = []
    while a:
        for i in range(len(a)):
            a[i][0] += a[i][1]

        if a[0][0] >= 100:
            count = 0
            while a:
                tempa = a.popleft()
                if tempa[0] >= 100:
                    count+=1
                else:
                    a.appendleft(tempa)
                    break

            answer.append(count)

    return answer
    