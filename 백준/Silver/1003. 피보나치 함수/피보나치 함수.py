import sys
n = int(sys.stdin.readline())
lis = []
for i in range(n):
    lis.append(int(sys.stdin.readline()))

f = [[0, 0]]*41
f[0] = [1, 0]
f[1] = [0, 1]

for i in lis:
    if i == 0:
        print("{} {}".format(f[0][0], f[0][1]))
    elif i == 1:
        print("{} {}".format(f[1][0], f[1][1]))
    else:
        for j in range(2, i+1):
            if f[j] == [0, 0]:
                f[j] = [(f[j-1][0]) + (f[j-2][0]), (f[j-1][1]) + (f[j-2][1])]
        print("{} {}".format(f[i][0], f[i][1]))