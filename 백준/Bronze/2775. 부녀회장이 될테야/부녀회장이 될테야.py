foi = int(input())
for w in range(foi):
    FlooR = int(input())
    NuM = int(input())
    NumlisT = [q for q in range(1, NuM+1)]
    for i in range(FlooR):
        for j in range(1, NuM):
            NumlisT[j] = NumlisT[j] + NumlisT[j - 1]
    print(NumlisT[NuM - 1])
