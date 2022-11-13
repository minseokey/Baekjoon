import math
n = int(input())
lis = []
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 중심간 거리
    dis = math.sqrt(abs(abs((x1 - x2)) ** 2 + abs((y1 - y2)) ** 2))
    if r1 - r2 >= 0:
        rmax = r1
        rmin = r2
    else:
        rmax = r2
        rmin = r1

    if x1 == x2 and y1 == y2 and r1 == r2:    # 동일한 원일때
        lis.append(-1)
    elif x1 == x2 and y1 == y2 and r1 != r2:   # 중심은 같지만 반지름만 다를때
        lis.append(0)
    elif dis > float(rmax):                           # 외접일때
        if float(r1 + r2) > dis:               # 만나지 않을때
            lis.append(2)
        elif float(r1 + r2) == dis:            # 외접 1점
            lis.append(1)
        elif float(r1 + r2) < dis:                                  # 외접 2점
            lis.append(0)
    elif dis == float(rmax):                          # 작은원의 중심이 큰원에 있을때 (무조건 2점이 만나용)
        lis.append(2)
    elif dis < float(rmax):                           # 내접일때
        if float(dis + rmin) > float(rmax):    # 두점에서
            lis.append(2)
        elif float(dis + rmin) == float(rmax):  # 한점에서 만날때
            lis.append(1)
        elif float(dis + rmin) < float(rmax):  # 안만날때
            lis.append(0)
    print(lis[i])