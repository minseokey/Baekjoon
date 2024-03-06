import sys

switch = int(sys.stdin.readline())
lis = [0] + list(map(int, sys.stdin.readline().split()))

stu = int(sys.stdin.readline())


def boy(num):
    for i in range(num, switch + 1, num):
        lis[i] = abs(lis[i] - 1)


def girl(num):
    top = num
    bot = num
    lis[top] = abs(lis[top] - 1)
    while True:
        if top + 1 <= switch and bot - 1 > 0:
            top += 1
            bot -= 1
            if lis[top] == lis[bot]:
                lis[top] = abs(lis[top] - 1)
                lis[bot] = abs(lis[bot] - 1)
            else:
                break
        else:
            break


for i in range(stu):
    gen, num = map(int, sys.stdin.readline().split())
    if gen == 1:
        boy(num)
    else:
        girl(num)

lis = lis[1:]
for i in range(0,len(lis), 20):
    print(*lis[i:i+20])
