import sys

paper = [5, 5, 5, 5, 5]
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

mini = float('inf')


def dfs(count):
    global mini
    if count >= mini:
        return
    key = False
    y, x = 0, 0
    for i in range(10):
        for j in range(10):
            if lis[i][j] == 1:
                key = True
                y, x = i, j
                break
        if key:
            break
    if not key:
        mini = count

    for size in range(5, 0, -1):
        fit = True
        if y + size <= 10 and x + size <= 10:
            for ti in range(y, y + size):
                for tj in range(x, x + size):
                    if lis[ti][tj] == 0:
                        fit = False
                        break
                if not fit:
                    break

            # 맞는 종이이다.
            if fit and paper[size - 1] > 0:
                for ti in range(y, y + size):
                    for tj in range(x, x + size):
                        lis[ti][tj] = 0
                paper[size - 1] -= 1
                dfs(count + 1)
                for ti in range(y, y + size):
                    for tj in range(x, x + size):
                        lis[ti][tj] = 1
                paper[size - 1] += 1


dfs(0)
if mini == float('inf'):
    print(-1)
else:
    print(mini)
