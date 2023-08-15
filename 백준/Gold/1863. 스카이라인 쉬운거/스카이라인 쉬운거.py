import sys

n = int(input())

stack = []
ans = 0
for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))[1]
    while stack and stack[-1] > temp:
        stack.pop()
        ans += 1
    if temp != 0 and (not stack or stack[-1] < temp):
        stack.append(temp)


ans += len(stack)
print(ans)