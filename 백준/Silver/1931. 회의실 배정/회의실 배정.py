N = int(input())
relis = []
for i in range(N):
    a, b = map(int, input().split())
    relis.append([a, b])

relis.sort(key = lambda x : (x[1],x[0]))
count = 0
before = 0
for i in relis:
    if i[0] >= before:
        before = i[1]
        count+=1

print(count)