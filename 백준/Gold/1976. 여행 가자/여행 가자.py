import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

lis = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    temp[i] = 1
    lis.append(temp)

plan = list(map(int, sys.stdin.readline().split()))
for i in range(len(plan)):
    plan[i] -= 1

df = [i for i in range(n)]


def find(a):
    if df[a] == a:
        return a
    else:
        return find(df[a])


def uniondetect(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        df[a] = b
    else:
        df[b] = a

# 경로 초기화
for i in range(len(lis)):
    for j in range(len(lis[i])):
        if lis[i][j] == 1:
            union(i,j)



start = plan[0]
end = 0
key = True
for i in range(1, m):
    end = plan[i]
    if uniondetect(start,end):
        pass
    else:
        key = False
        break

if key:
    print("YES")
else:
    print("NO")
