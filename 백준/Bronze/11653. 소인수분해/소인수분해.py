import math
num = int(input())
t = math.ceil(math.sqrt(num))
sqrtlis = []
solis = []
for i in range(1,t+1):
    b = 0
    for j in range(1,t+1):
        if i % j == 0:
            b = b + 1
    if b == 2:
        sqrtlis.append(i)
for i in sqrtlis:
    a = True
    while a:
        if num % i == 0:
            print(i)
            num = num / i
        else:
            a = False
if num != 1:
    print(int(num))
