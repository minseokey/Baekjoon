import sys

n = int(sys.stdin.readline())
lis = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dic = {2: 1, 3: 7, 4: 4, 5: 2, 6: 0, 7: 8}
for i in range(n):
    now = int(sys.stdin.readline())

    # 작은거
    small = now
    places = small // 7
    rests = small % 7

    if rests == 1:
        small = "10" + "8" * (places-1)
    elif rests == 2:
        small = "1" + "8" * places
    elif rests == 3:
        if not places:
            small = "7"
        elif places == 1:
            small = "22"
        else:
            small = "200" + "8" * (places-2)
    elif rests == 4:
        if not places:
            small = "4"
        else:
            small = "20" + "8" * (places-1)
    elif rests == 5:
        small = "2" + "8" * places
    elif rests == 6:
        small = "6" + "8" * places
    elif rests == 0:
        small = "8"* places

    # 큰거
    big = now
    placeb = big // 2
    restb = big % 2

    if restb == 1:
        big = ("7" + "1" * (placeb - 1))
    else:
        big = ("1" * placeb)

    print(small, big)
