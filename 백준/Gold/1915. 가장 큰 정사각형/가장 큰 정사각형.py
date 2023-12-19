import sys

y,x = map(int,sys.stdin.readline().split())

field = []
for _ in range(y):
    lis = list(map(int,list(sys.stdin.readline().strip())))
    field.append(lis)

for i in range(1,y):
    for j in range(1,x):
        if field[i-1][j-1] != 0 and field[i-1][j] != 0 and field[i][j-1]!= 0 and field[i][j] != 0:
            field[i][j] = int(min(field[i-1][j-1], field[i][j-1], field[i-1][j])) + 1

maxx = 0
for i in field:
    maxx = max(maxx, max(i))
print(maxx**2)