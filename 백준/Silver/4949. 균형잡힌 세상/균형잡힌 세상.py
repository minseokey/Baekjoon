import sys

while (True):
    a = sys.stdin.readline()
    arr = []
    tester = True
    fooot = False
    dic = {"}":"{",")":"(","]":"["}
    for i in range(len(a)):
        if a[0] == ".":
            fooot = True
            break
        elif a[i] in dic.values():
            arr.append(a[i])
        elif a[i] in dic.keys():
            if len(arr) == 0:
                tester = False
                break
            elif arr[-1] == dic[a[i]]:
                del arr[-1]
            else:
                tester = False
                break
        elif a[i] == ".":
            break
    if fooot == True:
        pass
    elif tester and len(arr) == 0:
        print("yes")
    else:
        print("no")

    if fooot:
        break