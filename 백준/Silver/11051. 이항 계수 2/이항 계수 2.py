import sys

n, k = map(int, sys.stdin.readline().split())

field = [[1]]

for i in range(1, n + 1):
    lis = []
    for j in range(i + 1):
        if j == 0:
            lis.append((field[i - 1][j]))
        elif j == i:
            lis.append((field[i - 1][j - 1]))
        else:
            lis.append((field[i - 1][j] + field[i - 1][j - 1]) % 10007)
    field.append(lis)

print(field[n][k])
