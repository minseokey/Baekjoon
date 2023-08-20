import copy
import sys


def mul(num, lis, temp):
    if num == temp:
        return lis
    nowlis = []
    for t in [" ", "+", "-"]:
        newlis = copy.deepcopy(lis)
        for mini in newlis:
            mini.insert((num * 2) + 1, t)
            nowlis.append(mini)
    return mul(num + 1, nowlis, temp)

def calc(lis, ind):
    ans = 0
    stack = []
    last = ""
    for q in lis:
        if q in ["-", "+"]:
            num = int("".join(stack))
            stack.clear()
            if last == "":
                ans = num
            else:
                if last == "+":
                    ans += num
                elif last == "-":
                    ans -= num
            last = q
        else:
            stack.append(q)

    if last == "+":
        ans += int("".join(stack))
    elif last == "-":
        ans -= int("".join(stack))
    else:
        ans = int(lis)

    if ans == 0:
        anslis.append(ind)


n = int(sys.stdin.readline())
for i in range(n):
    temp = int(sys.stdin.readline())
    original = [str(i) for i in range(1, temp + 1)]
    aru = mul(0, [original], temp-1)

    newaru = copy.deepcopy(aru)
    for j in range(len(aru)):
        aru[j] = "".join(aru[j]).replace(" ","")
        newaru[j] = "".join(newaru[j])

    anslis = []

    for j in range(len(aru)):
        calc(aru[j],j)

    rel = []
    for j in anslis:
        rel.append(newaru[j])

    rel.sort()
    for j in rel:
        print(j)
    print()

