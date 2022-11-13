import sys
n,need = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))

tree.sort(reverse = True)
tree.append(0)
kk = True
tempp,numberlevels,counter = 0,0,0
for i in range (1,n+1):
    tempp = numberlevels
    numberlevels += ((tree[i-1] - tree[i]) * i)
    if numberlevels == need:
        print(tree[i])
        break
    elif numberlevels > need:
        while True:
            counter+=1
            if tempp+(counter*i) >= need:
                print(tree[i-1] - counter)
                kk = False
                break
        if not kk:
            break



