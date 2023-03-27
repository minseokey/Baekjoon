import sys

exp = sys.stdin.readline().strip()

ans = []
stack = []
for i in exp:
    if i.isalpha():
        ans.append(i)

    elif i in ["+","-"]:
        temp = []
        while stack:
            kk = stack.pop()
            if kk in ["*","/","+","-"]:
                temp.append(kk)
            else:
                stack.append(kk)
                break
        stack.append(i)
        ans += temp

    elif i in ["*","/"]:
        temp = []
        while stack:
            kk = stack.pop()
            if kk in ["*","/"]:
                temp.append(kk)
            else:
                stack.append(kk)
                break
        stack.append(i)
        ans += temp

    elif i == "(":
        stack.append(i)

    elif i == ")":
        temp = []
        while stack:
            kk = stack.pop()
            if kk == "(":
                break
            else:
                temp.append(kk)

        ans += temp

ans += reversed(stack)
print("".join(ans))






