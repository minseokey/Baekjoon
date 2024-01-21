import itertools
import sys

n, k = map(int, sys.stdin.readline().split())

basic = ["a", "n", "t", "c", "i"]
def bitTrans(word):
    ret = 0
    visited = [False] * 26
    for i in word:
        temp = ord(i) - 97
        if not visited[temp]:
            ret += 2 ** (temp)
            visited[temp] = True
    return ret


def makeDiff(itert):
    nownum = basicNum
    for i in itert:
        nownum += 2**i
    return nownum

def diff(nowbit):
    ans = 0
    for i in alllis:
        if not (i & ~nowbit):
            ans += 1
    return ans

if k < 5:
    print(0)
else:
    k -= 5
    alllis = []
    basic_n = [ord("a") - 97, ord("c") - 97, ord("i") - 97, ord("n") - 97, ord("t") - 97]
    basicNum = bitTrans(basic)
    maxx = 0
    for i in range(n):
        alllis.append(bitTrans(sys.stdin.readline().strip()))

    alplis = [i for i in range(26) if i not in basic_n]

    itert = list(itertools.combinations(alplis,k))

    for i in itert:
        maxx = max(maxx, diff(makeDiff(i)))

    print(maxx)


