t = True
while t:
    lis = list(map(int, input().split()))
    c = max(lis)
    lis.remove(c)
    a = lis[0]
    b = lis[1]
    if a == 0 and b == 0 and c == 0:
        t = False
    else:
        if a ** 2 + b ** 2 == c ** 2:
            print("right")
        else:
            print("wrong")