def solution(routes):
    routes.sort()
    print(routes)
    i = 0
    count = 1
    while i < len(routes):
        maxa = routes[i][0]
        maxb = routes[i][1]
        keyy = False
        for j in range(i + 1,len(routes)):
            if maxb >= routes[j][0]:
                maxa = max(maxa,routes[j][0])
                maxb = min(maxb,routes[j][1])
                pass
            else:
                maxa = routes[j][0]
                maxb = routes[j][1]
                count += 1
                i = j
                keyy = True
                break
        if not keyy:
            break
    return count