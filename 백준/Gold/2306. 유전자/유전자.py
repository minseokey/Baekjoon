import sys

dna = list(sys.stdin.readline().strip())
leng = len(dna)
presum = [[0] * leng for _ in range(leng)]

if leng == 1:
    print(0)
elif leng == 2:
    if dna == ["a", "t"] or dna == ["g", "c"]:
        print(2)
    else:
        print(0)
else:
    for i in range(leng):
        if dna[i] == "a":
            temp = i+1
            while temp < leng:
                if dna[temp] == "t":
                    presum[i][temp] = 1
                    break
                temp += 1

        elif dna[i] == "g":
            temp = i+1
            while temp < leng:
                if dna[temp] == "c":
                    presum[i][temp] = 1
                    break
                temp += 1

    def inside(s, e):
        ans = presum[s][e]
        for i in range(s, e):
            ans = max(ans, presum[s][i] + presum[i + 1][e])

        return ans

    for gap in range(3, leng):  # 간격
        for start in range(leng - gap):
            end = start + gap
            if (dna[start] == "a" and dna[end] == "t") or (dna[start] == "g" and dna[end] == "c"):
                presum[start][end] = max(presum[start][end], inside(start+1, end-1) + 1)
            presum[start][end] = max(presum[start][end], inside(start, end))

    maxx = 0
    for i in presum:
        maxx = max(max(i), maxx)

    print(maxx * 2)
