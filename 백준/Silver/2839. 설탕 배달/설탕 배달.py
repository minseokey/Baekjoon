tot = int(input())
foi = 0
while True:
    if tot % 5 != 0:
        tot = tot - 3
        foi = foi + 1
        if tot == 0:
            print(foi)
            break
        elif tot < 0:
            print(-1)
            break
    elif tot % 5 == 0:
        tot = tot - 5
        foi = foi + 1
        if tot == 0:
            print(foi)
            break
