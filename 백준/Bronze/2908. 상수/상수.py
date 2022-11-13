a,b = map(str,input().split())
alis = []
blis = []
for i in range(0,3):
    alis.append(a[2-i])
    blis.append(b[2-i])
aa = int("".join(alis))
bb = int("".join(blis))
if aa - bb > 0 :
    print(aa)
else:
    print(bb)