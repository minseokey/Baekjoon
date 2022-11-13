import sys
n = int(sys.stdin.readline())
lis = list(input().split())
newi = []
for i in lis:
    newi.append(int(i))
numset = set(newi)
liso = sorted(list(numset))
dic = dict()
for i in range(len(liso)):
    dic[liso[i]] = i

for i in range(n):
    print(dic.get(newi[i]),end = " ")