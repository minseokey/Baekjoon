import collections,sys
stack = collections.deque()
n = int(input())
for i in range(n):
    temp = sys.stdin.readline().strip("\n").split(" ")

    if temp[0] == "push":
        stack.append(temp[1])


    elif temp[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)


    elif temp[0] == "size":
        print(len(stack))


    elif temp[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)


    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)