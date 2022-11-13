a = True
while a:
    n = int(input())
    if n == 0:
        a = False
    else:
        lis = [False, False]+[True]*(2*n-1)
        prilis = []
        priliss = []
        for i in range(2, 2*n + 1):
            if lis[i]:
                prilis.append(i)
                for j in range(2*i, 2*n + 1, i):
                    lis[j] = False
        for i in prilis:
            if i > n:
                priliss.append(i)
        print(len(priliss))