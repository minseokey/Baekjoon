import sys


n = int(sys.stdin.readline())
lis = []
t = 0
for i in range(n):
    a,b = sys.stdin.readline().strip().split(" ")
    lis.append([a,b,t])
    t = t +1
#그냥 소트에 조건을 걸자...


lis.sort(key = lambda x :(int(x[0]),x[2]))
# 람다식을 이용함으로써 그 요소의 0번쨰인덱스와 2번쨰 인덱스만을 sort한다 라고 알려줌
for i in lis:
    print("{} {}".format(i[0],i[1]))
