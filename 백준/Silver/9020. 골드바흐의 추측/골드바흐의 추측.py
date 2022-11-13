nn = int(input())
nlist = []
for q in range(nn):
    n = int(input())
    nlist.append(n)
nmax = max(nlist)
lis = [False, False] + [True]*(nmax-1)
prilis = []
for i in range(2 , nmax + 1):
    if lis[i]:
        prilis.append(i)
    for j in range(2*i,nmax+1,i):
        lis[j] = False
for j in nlist:
    llis = [0, 0]
    for i in prilis:
        if i <= j/2 and j-i in prilis:
            llis[0] = i
            llis[1] = j-i
    print("{} {}".format(llis[0], llis[1]))
