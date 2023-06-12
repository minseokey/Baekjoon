import sys

fois = int(sys.stdin.readline())
for i in range(fois):
    n = int(sys.stdin.readline())
    lis = list(sys.stdin.readline().split())

    codelis = []
    for j in lis:
        temp = 0
        if j[0] == "E":
            temp += 1
        if j[1] == "S":
            temp += 2
        if j[2] == "T":
            temp += 4
        if j[3] == "P":
            temp += 8
        codelis.append(temp)

    anslis = []
    if n > 32:
        print(0)
    else:
        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j + 1,n):
                    anslis.append(bin(codelis[i] ^ codelis[j]).count("1") + bin(codelis[j] ^ codelis[k]).count("1") + bin(codelis[k] ^ codelis[i]).count("1"))

        print(min(anslis))
