import sys

fois = int(sys.stdin.readline())

if fois in [1,2]:
    print(1)
elif fois == 0:
    print(0)

else:
    n = [0 for i in range(fois + 1)]
    n[0] = 0
    n[1] = 1
    n[2] = 1


    for i in range(2,fois + 1):
        n[i] = n[i-2] + n[i-1]

    print(n[-1])