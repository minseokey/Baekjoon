lisx = []
lisy = []

for i in range(3):
    x, y = map(int,input().split())
    if x in lisx:
        lisx.remove(x)
    else:
        lisx.append(x)
    if y in lisy:
        lisy.remove(y)
    else:
        lisy.append(y)


print(lisx[0],lisy[0])