import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

apple = []
for i in range(k):
    y, x = map(int, sys.stdin.readline().split())
    apple.append((y - 1, x - 1))

l = int(sys.stdin.readline())
move = deque()
for i in range(l):
    x, c = map(str, sys.stdin.readline().split())
    move.append((int(x), c))

# dir,y,x,count
snake = deque()
snake.append([0, 0])
size = 1
run = 1
nowdir = [0, 1]
key = True
while True:
    y, x = snake[0]
    y += nowdir[0]
    x += nowdir[1]
    appleate = False
    if 0 <= y < n and 0 <= x < n and ([y, x] not in snake):
        if move and move[0][0] == run:
            if move[0][1] == "D":
                if nowdir == [0, 1]:
                    nowdir = [1, 0]
                elif nowdir == [1, 0]:
                    nowdir = [0, -1]
                elif nowdir == [0, -1]:
                    nowdir = [-1, 0]
                elif nowdir == [-1, 0]:
                    nowdir = [0, 1]

            elif move[0][1] == "L":
                if nowdir == [0, 1]:
                    nowdir = [-1, 0]
                elif nowdir == [1, 0]:
                    nowdir = [0, 1]
                elif nowdir == [0, -1]:
                    nowdir = [1, 0]
                elif nowdir == [-1, 0]:
                    nowdir = [0, -1]
            move.popleft()

        if (y, x) in apple:
            appleate = True
            apple.remove((y, x))
        snake.appendleft([y, x])
        if not appleate:
            snake.pop()
        else:
            size += 1
        run += 1
    else:
        key = False

    if not key:
        break

print(run)
