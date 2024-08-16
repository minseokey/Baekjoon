import sys

n = int(sys.stdin.readline())

t = n%7
if t in [1,3,4,5,6]:
    print("SK")
else:
    print("CY")