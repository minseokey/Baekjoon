import sys

length = "I" + "OI" * (int(sys.stdin.readline().strip()))
n = int(sys.stdin.readline().strip())
t = sys.stdin.readline().strip()

count = 0
i = 0
while i <= n - len(length):
    if t[i] == "O":
        i += 1
        pass
    elif t[i:i+len(length)] == length:
        count += 1
        i += 2
    else:
        i += 1

print(count)