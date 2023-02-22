import copy


def solution(rectangle, characterX, characterY, itemX, itemY):
    main = [[0 for i in range(102)] for j in range(102)]
    for i in rectangle:
        for y in range(2 * i[1], 2 * i[3]):
            for x in range(2 * i[0], 2 * i[2]):
                main[y][x] = 1
                main[y + 1][x] = 1
                main[y][x + 1] = 1
                main[y + 1][x + 1] = 1

    for y in range(len(main)):
        for x in range(len(main[y])):
            if (main[y][x] == 1) and (
                    (x > 0 and y > 0 and main[y - 1][x - 1] == 0) or (
                    x > 0 and y < 102 and main[y + 1][x - 1] == 0) or (
                    y > 0 and x < 102 and main[y - 1][x + 1] == 0) or (
                    y < 102 and x < 102 and main[y + 1][x + 1] == 0) or (
                    x > 0 and main[y][x - 1] == 0) or (
                    x < 102 and main[y][x + 1] == 0) or (
                    y > 0 and main[y - 1][x] == 0) or (
                    y < 102 and main[y + 1][x] == 0)):
                main[y][x] = 2

    a = []

    def road(check, nowx, nowy, count):

        if nowx == itemX * 2 and nowy == itemY * 2:
            a.append(count)
            return
        if y > 0 and main[nowy - 1][nowx] == 2 and check[nowy - 1][nowx]:
            newcheck = copy.deepcopy(check)
            newcheck[nowy - 1][nowx] = False
            road(newcheck, nowx, nowy - 1, count + 1)

        if y < 102 and main[nowy + 1][nowx] == 2 and check[nowy + 1][nowx]:
            newcheck = copy.deepcopy(check)
            newcheck[nowy + 1][nowx] = False
            road(newcheck, nowx, nowy + 1, count + 1)

        if x > 0  and main[nowy][nowx - 1] == 2 and check[nowy][nowx - 1]:
            newcheck = copy.deepcopy(check)
            newcheck[nowy][nowx - 1] = False
            road(newcheck, nowx - 1, nowy, count + 1)

        if x < 102 and main[nowy][nowx + 1] == 2 and check[nowy][nowx + 1]:
            newcheck = copy.deepcopy(check)
            newcheck[nowy][nowx + 1] = False
            road(newcheck, nowx + 1, nowy, count + 1)

    road([[True for i in range(102)] for j in range(102)], characterX * 2, characterY * 2, 0)

    return min(a) // 2