n = int(input())
lis = [[[-1] for i in range(10)] for j in range(n - 1)]
lis.append([[0],[1],[1],[1],[1],[1],[1],[1],[1],[1]])
cunt = 0
t = 0
def stair(foi,num):
    if num == 0:
        if lis[foi][0][0] != -1:
            pass
        else:
            lis[foi][0][0] = lis[foi + 1][1][0]

    elif num == 9:
        if lis[foi][9][0] != -1:
            pass
        else:
            lis[foi][9][0] = lis[foi + 1][8][0]

    else:
        if lis[foi][num][0] != -1:
            pass
        else:
            lis[foi][num][0] = lis[foi + 1][num + 1][0] + lis[foi + 1][num - 1][0]



for j in range(n - 1, -1, -1):
    for i in range(0, 10):
        stair(j, i)
for i in range(10):
    t = lis[0][i][0] + t
print(t % 1000000000)