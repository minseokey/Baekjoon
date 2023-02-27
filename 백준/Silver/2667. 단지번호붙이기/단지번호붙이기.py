import sys

n = int(sys.stdin.readline())
lis = []
for i in range(n):
    temp = sys.stdin.readline().strip()
    lis.append([x for x in temp])

check = [[True for i in range(n)] for j in range(n)]
ans = dict()


def recur(y, x, vil):
    ans[vil] += 1
    if y > 0 and check[y - 1][x] and lis[y - 1][x] == '1':
        check[y - 1][x] = False
        lis[y - 1][x] = vil
        recur(y - 1, x, vil)
    if x > 0 and check[y][x - 1] and lis[y][x - 1] == '1':
        check[y][x - 1] = False
        lis[y][x - 1] = vil
        recur(y, x - 1, vil)
    if y < n - 1 and check[y + 1][x] and lis[y + 1][x] == '1':
        check[y + 1][x] = False
        lis[y + 1][x] = vil
        recur(y + 1, x, vil)
    if x < n - 1 and check[y][x + 1] and lis[y][x + 1] == '1':
        check[y][x + 1] = False
        lis[y][x + 1] = vil
        recur(y, x + 1, vil)


t = 2
for i in range(n):
    for j in range(n):
        if lis[i][j] == '1' and check[i][j]:
            check[i][j] = False
            ans[t] = 0
            lis[i][j] = t
            recur(i, j, t)
            t += 1

print(len(ans.values()))
for i in sorted(ans.values()):
    print(i)