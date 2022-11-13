maxx, alw = map(int, input().split())


arr = []
count, i = 0, 0
maxxx = [d for d in range(1, maxx+1)]

while(True):
    i += 1
    if len(maxxx) == 1:
        arr.append(maxxx[0])
        break
    if i == alw:
        arr.append(maxxx[count])
        maxxx.remove(maxxx[count])
        i = 0
    else:
        count += 1
        if count == len(maxxx):
            count = 0
        elif count > len(maxxx):
            count = 1



print("<",end = "")
for i in range(len(arr) - 1):
    print(arr[i],end = "")
    print(", ",end="")
print(arr[-1],end = "")
print(">",end = "")

