import copy
from collections import Counter


def solution(name):
    boollist = []
    answer = 0
    for i in range(len(name)):
        boollist.append(False if min(ord(name[i]) - ord("A"), 26 - (ord(name[i]) - ord("A"))) == 0 else True)
        answer += min(ord(name[i]) - ord("A"), 26 - (ord(name[i]) - ord("A")))

    if len(Counter(boollist)) == 1 and boollist[0]:
        answer += len(boollist) - 1
        return answer
    elif len(Counter(boollist)) == 1 and not boollist[0]:
        return 0

    minn = [float('inf')]
    def recur(k, now, count):
        if len(Counter(k)) == 1:
            minn.append(count)
        for i in range(1, len(boollist)):
            mink = now + i if now + i < len(boollist) else (now + i) - len(boollist)
            if k[mink]:
                newk = copy.copy(k)
                newk[mink] = False
                if count+1 > min(minn):
                    break
                recur(newk, mink, count + i)
        for i in range(1, len(boollist)):
            maxk = now - i if now - i >= 0 else len(boollist) + (now - i)
            if k[maxk]:
                newk = copy.copy(k)
                newk[maxk] = False
                if count+1 > min(minn):
                    break
                recur(newk,maxk, count + i)

    boollist[0] = False
    recur(boollist, 0, 0)
    return min(minn) + answer

print(solution("AAAAAAAAAAAA"))