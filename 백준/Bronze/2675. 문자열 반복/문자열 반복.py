n = int(input())
while True:
    try:
        lis = []
        anslis = []
        a, b = map(str, input().split())
        numa = int(a)

        for i in range(0,len(b)):
            lis.append(b[i])

        for j in range(0,len(b)):
            for k in range(0,numa):
                anslis.append(b[j])
        print("".join(anslis))
    except EOFError:
        break