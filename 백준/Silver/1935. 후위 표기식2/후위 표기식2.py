import sys
from collections import deque

n = int(sys.stdin.readline())
calc = deque(list(sys.stdin.readline().strip()))
calcoff = ["+","-","*","/"]
num = dict()
start = ord("A")
for _ in range(n):
    num[chr(start)] = int(sys.stdin.readline())
    start += 1

stack = []
while calc:
    nn = calc.popleft()
    if nn in calcoff:
        number1 = stack.pop()
        number2 = stack.pop()
        if nn == "+":
            stack.append(number2+number1)
        if nn == "-":
            stack.append(number2-number1)
        if nn == "*":
            stack.append(number2*number1)
        if nn == "/":
            stack.append(number2/number1)
    else:
        stack.append(num[nn])

print("{:.2f}".format(float(stack[0])))