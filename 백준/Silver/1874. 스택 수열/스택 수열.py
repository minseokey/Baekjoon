n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

num = 1
newlis = []
addlis = []
a = True
for i in range(len(arr)):
    if not a:
        print("NO")
        break
    assenticnum = arr[i]
    while(True):
        if newlis and newlis[-1] == assenticnum:
            newlis.pop()
            addlis.append("-")
            break
        else:
            newlis.append(num)
            addlis.append("+")
            if num > n:
                a = False
                break
            else:
                num += 1

if a:
    for i in addlis:
        print(i)