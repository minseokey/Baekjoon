def solution(n, results):
    floyd = [[0 for i in range(n)] for j in range(n)]
    for i in results:
        floyd[i[0] - 1][i[1] - 1] = 2
        floyd[i[1] - 1][i[0] - 1] = 1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j != k and i != k and i != j:
                    if floyd[j][k] == 0:
                        if floyd[j][i] == 2 and floyd[i][k] == 2:
                            floyd[j][k] = 2
                        if floyd[j][i] == 1 and floyd[i][k] == 1:
                            floyd[j][k] = 1
    num = 0
    for i in floyd:
        print(i, i.count(0))
        if i.count(0) == 1:
            num += 1

    return num