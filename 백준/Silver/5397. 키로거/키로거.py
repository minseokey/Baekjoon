import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    inputt = list(sys.stdin.readline().strip())
    string = deque()
    end_string = deque()
    for j in range(len(inputt)):
        if inputt[j] == "<":
            if string:
                end_string.appendleft(string.pop())

        elif inputt[j] == ">":
            if end_string:
                string.append(end_string.popleft())

        elif inputt[j] == "-":
            if string:
                string.pop()

        else:
            string.append(inputt[j])

    print("".join(string) + "".join(end_string))

