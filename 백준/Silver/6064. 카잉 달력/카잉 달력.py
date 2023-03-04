import sys
from math import gcd

lis = []
for i in range(int(sys.stdin.readline().strip())):
    lis.append((list(map(int, sys.stdin.readline().split()))))

for i in lis:
    num = 0
    if abs(i[3] - i[2]) % gcd(i[1], i[0]) != 0:
        print(-1)
    else:
        while True:
            if ((i[1] * num) + (i[3] - i[2])) % i[0] == 0:
                print(((i[1] * num) + i[3]))
                break

            num += 1