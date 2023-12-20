import sys

n = int(sys.stdin.readline())

stack = []
count = 0
for _ in range(n):
    now = int(sys.stdin.readline())
    i = len(stack) - 1
    key = True
    while i >= 0:
        if stack[i][0] > now:
            count += 1
            break
        elif stack[i][0] < now:
            count += stack.pop()[1]
            i -= 1
        else:
            count += stack[i][1]
            stack[i][1] += 1
            i -= 1
            key = False
    if key:
        stack.append([now, 1])

print(count)