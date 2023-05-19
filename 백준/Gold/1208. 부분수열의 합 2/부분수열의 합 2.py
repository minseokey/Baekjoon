import bisect
import itertools
import sys

leng, target = map(int,sys.stdin.readline().split())
origin = list(map(int,sys.stdin.readline().split()))
clusA = origin[:leng//2]
clusB = origin[leng//2:]
ans = 0
def mapping(clus):
    temp = []
    for i in range(len(clus) + 1):
        for j in itertools.combinations(clus,i):
            temp.append(sum(j))
    return temp
combA = sorted(mapping(clusA))
combB = sorted(mapping(clusB))
for i in combA:
    B_Target = target - i
    start = bisect.bisect_left(combB,B_Target)
    end = bisect.bisect_right(combB,B_Target)
    ans += end - start
# 모두 안고르는 경우 제
if target == 0:
    ans -= 1
print(ans)

