import math
a = int(input())
b = int(input())
sqrtnum = math.sqrt(b)
sqrtlis = []
numlis = [p for p in range(a,b+1)]
if 1 in numlis:
    numlis.remove(1)
newlis = list.copy(numlis)
ans = 0
for i in range(1, math.ceil(sqrtnum)+1):
    n = 0
    for j in range(1, math.ceil(sqrtnum)+1):
        if i % j == 0:
            n = n + 1
    if n == 2:
        sqrtlis.append(i)

for w in numlis:
    for q in sqrtlis:
        if w % q == 0 and w not in sqrtlis:
            newlis.remove(w)

            break

if len(newlis) == 0:
    print(-1)
else:
    for i in range(len(newlis)):
        ans = ans + newlis[i]
    print(ans)
    print(min(newlis))
