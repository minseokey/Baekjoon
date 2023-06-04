import bisect
import sys

sys.setrecursionlimit(10 ** 9)
n, m, k = map(int, sys.stdin.readline().split())
minsu = list(map(int, sys.stdin.readline().split()))
chulsu = list(map(int, sys.stdin.readline().split()))

minsu.sort()

uf = [i for i in range(m +1)]


# unionfind
def union(a, b):
    # b가 큰거
    a = find(a)
    b = find(b)
    uf[a] = b


def find(ind):
    if ind == uf[ind]:
        return ind
    uf[ind] = find(uf[ind])
    return uf[ind]


for i in range(k):
    tidx = bisect.bisect_right(minsu, chulsu[i])
    temp = find(tidx)
    print(minsu[temp])
    union(temp, temp + 1)
