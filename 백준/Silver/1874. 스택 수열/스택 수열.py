import sys

n = int(sys.stdin.readline())
t_lis = [int(sys.stdin.readline()) for _ in range(n)]
t_lis.reverse()
stack = []
ans = []
for i in range(1,n+1):
    while stack:
        if t_lis[-1] == stack[-1]:
            t_lis.pop()
            stack.pop()
            ans.append("-")
        else:
            break
    stack.append(i)
    ans.append("+")

# 마지막 추가로
while stack:
    if t_lis[-1] == stack[-1]:
        t_lis.pop()
        stack.pop()
        ans.append("-")
    else:
        break

if stack:
    print("NO")
else:
    for p in ans:
        print(p)



