n = int(input())
a = [(i+1)**2 for i in range(224)]
k = False
num = 4
for i in a:
    if i == n:
        num = min(1,num)
        k = False
    elif i > n:
        break

    for j in a:
        if i + j == n:
            num = min(2,num)
            k = False
        elif i+j > n:
            break

        for k in a:
            if i + j + k == n:
                num = min(3,num)
                k = False
            elif i + j + k > n:
                break

        if not k:
            break

    if not k:
        break


print(num)