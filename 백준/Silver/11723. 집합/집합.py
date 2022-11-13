import sys
n = int(sys.stdin.readline())
a = set()
for i in range(n):
    text = sys.stdin.readline().split()

    if text[0] == "add":
        a.add(text[1])
    elif text[0] == "remove":
        if text[1] in a:
            a.remove(text[1])
    elif text[0] == "check":
        if text[1] in a:
            print(1)
        else:
            print(0)
    elif text[0] == "toggle":
        if text[1] in a:
            a.remove(text[1])
        else:
            a.add(text[1])
    elif text[0] == "all":
        temp = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
        a = set(temp)
    elif text[0] == "empty":
        a.clear()