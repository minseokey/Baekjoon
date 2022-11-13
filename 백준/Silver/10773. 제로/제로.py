import collections,sys
stack = collections.deque()
num1 = 0
num2 = 0
n = int(sys.stdin.readline())
for i in range(n):
    temp = int(sys.stdin.readline())
    if temp != 0:
        stack.append(temp)
        num1 += temp
    else:
        num2 += stack.pop()

print(num1 - num2)