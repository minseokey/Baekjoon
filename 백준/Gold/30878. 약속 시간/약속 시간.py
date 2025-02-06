import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


M = int(sys.stdin.readline().strip())

a = M * M * (90 - M)
b = 108000

g = gcd(a, b)
print(f"{a // g}/{b // g}")


