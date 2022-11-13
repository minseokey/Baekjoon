n = int(input())

listen = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def lastnumcheck(a):
    try:
        listen.append(listen[a - 1] + listen[a - 5])
    except IndexError:
        lastnumcheck(a - 1)


for i in range(n):
    num = int(input())
    while True:
        try:
            print(listen[num])
            break
        except IndexError:
            lastnumcheck(num)