n, m = map(int, input().split())
lisCard = input().split()
lis = []
lisnum = []
for i in lisCard:
    for j in lisCard:
        for k in lisCard:
            if i != j and j != k and  k != i:
                if int(i) + int(j) + int(k) - m <= 0:
                    lis.append(abs(int(i) + int(j) + int(k) - m))
                    lisnum.append(int(i) + int(j) + int(k))
q = lis.index(min(lis))
print(lisnum[q])