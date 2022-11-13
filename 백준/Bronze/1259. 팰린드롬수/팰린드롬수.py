while(1):
    num = input()
    if num == "0":
        break
    else:
        t = True
    for i in range(len(num)):
        if num[i] != num[len(num) - i - 1]:
            print("no")
            t = False
            break
    if t:
        print("yes")