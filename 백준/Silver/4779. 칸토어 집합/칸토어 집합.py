import sys
def cantour(n):
    if n > 0:
        return cantour(n-1) + [" "] * (3 ** (n-1)) + cantour(n-1)
    else:
        return ["-"]

while True:
    try:
        k = int(sys.stdin.readline())
        print("".join(cantour(k)))
    except:
        break

