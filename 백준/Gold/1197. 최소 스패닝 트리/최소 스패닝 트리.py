import sys
from collections import deque

v,e = map(int,sys.stdin.readline().split())
lis = []
for i in range(e):
    start,end,wei = map(int,sys.stdin.readline().split())
    lis.append([start-1,end-1,wei])
    lis.append([end-1,start-1,wei])

lis.sort(key = lambda x : x[2])
parentlis = [i for i in range(v)]

# 부모가 같니? 같다면 True, 다르면 이제부터 부모는 같게하고(연결) False
def find(a,b):
    tempa = parent(a)
    tempb = parent(b)

    if tempa > tempb:
        parentlis[tempa] = tempb
        return True
    elif tempa < tempb:
        parentlis[tempb] = tempa
        return True
    else:
        return False

# 부모가 누구니
def parent(temp):
    if parentlis[temp] == temp:
        return temp
    return parent(parentlis[temp])


ans = 0
for i in lis:
    if find(i[0],i[1]):
        ans += i[2]

print(ans)
