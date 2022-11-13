import math
a,b,c = map(int,input().split())
if (c-b) <= 0:
    print(-1)
else:
    k = a/(c-b)
    if k == 0:
        k = k+1
    elif k%1 == 0:
        k = k +1
    print(math.ceil(k))