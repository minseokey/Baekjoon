foi = int(input())
for k in range(0,foi):
    h, w, n = map(int, input().split())
    t = 0
    for i in range(0,w):
        for j in range(0,h):
            roonmun = (i + 1) + (100 * (j+1))
            t = t + 1
            if t == n:
                print(roonmun)
                break