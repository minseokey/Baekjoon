n = int(input())
whl = []
for i in range(n):
    a, b = map(int, input().split())
    whl.append([a,b,1])
for i in range(n):
    for j in range(n):
        if whl[i][0] < whl[j][0] and whl[i][1] < whl[j][1]:
            whl[i][2] = whl[i][2] + 1
for i in range(n):
    print((str(whl[i][2])), end = " ")