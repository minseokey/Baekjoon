import sys

n = int(sys.stdin.readline())
sys.setrecursionlimit(100000)

orilis = dict()
for i in range(1, n + 1):
    al = list(map(int, sys.stdin.readline().split()))
    ind = al[0]
    parse = al[1:-1]

    for j in range(0, len(parse), 2):
        if ind in orilis.keys():
            orilis[ind].append([parse[j], parse[j + 1]])
        else:
            orilis[ind] = [[parse[j], parse[j + 1]]]


def recur(check, nownode, weight):
    checklis[nownode] = max(checklis[nownode], weight)
    for a in orilis[nownode]:
        if not check[a[0]]:
            check[a[0]] = True
            recur(check, a[0], weight + a[1])


# 아무거나 기준으로 가장 먼거 찾기

check = [False for w in range(n + 1)]
check[1] = True
checklis = [0 for i in range(n + 1)]
recur(check, 1, 0)



# 가장 먼거 기준으로 반대쪽 가장 먼거 찾기
check1 = [False for w in range(n + 1)]
check1[checklis.index(max(checklis))] = True
recur(check1, checklis.index(max(checklis)), 0)


print(max(checklis))