n = int(input())
lis = []
for i in range(n):
    a,b = map(int, input().split())
    lis.append([a,b])

# 정렬 만들기... 소트 쓸까?

#for i in range(n):
slis = sorted(lis)
for i in slis:
    print("{} {}".format(i[0],i[1]))