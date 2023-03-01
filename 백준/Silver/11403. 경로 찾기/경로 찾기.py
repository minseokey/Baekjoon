import sys

n = int(sys.stdin.readline().strip())
lis = []
for i in range(n):
    lis.append(list(map(str,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if lis[j][i] == "1" and lis[i][k] == "1":
                lis[j][k] = "1"

for i in lis:
    print(" ".join(i))