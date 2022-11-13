import sys
n = int(sys.stdin.readline())
a = 1
b = 2
if n == 1:
    print(1)
else:
    for i in range(2,n):
        a, b = b, (a + b) % 15746
    print(b)