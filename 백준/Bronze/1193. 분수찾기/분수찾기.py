n = int(input()) - 1
t = 0
while True:
    t = t + 1
    n = n - t
    if n == -1:
        print("{}/{}".format(1,1))
        break
    if n < t + 1:
        a = t - n + 1
        b = n + 1
        if t % 2 == 0:
            print("{}/{}".format(a,b))
            break
        elif t % 2 == 1:
            print("{}/{}".format(b,a))
            break
