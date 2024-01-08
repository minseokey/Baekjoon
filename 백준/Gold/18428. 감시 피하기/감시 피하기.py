import sys

n = int(sys.stdin.readline())
lis = [sys.stdin.readline().split() for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


# 3개 백트래킹 조지자

def check():
    for i in range(n):
        for j in range(n):
            if lis[i][j] == "T":
                ty = i
                tx = j
                while ty < n - 1:
                    if lis[ty + 1][tx] not in ["S","O"]:
                        ty += 1
                    elif lis[ty + 1][tx] == "S":
                        return False
                    else:
                        break

                ty = i
                tx = j
                while tx < n - 1:
                    if lis[ty][tx + 1] not in ["S","O"]:
                        tx += 1
                    elif lis[ty][tx + 1] == "S":
                        return False
                    else:
                        break

                ty = i
                tx = j
                while 1 <= ty:
                    if lis[ty - 1][tx] not in ["S","O"]:
                        ty -= 1
                    elif lis[ty - 1][tx] == "S":
                        return False
                    else:
                        break

                ty = i
                tx = j
                while 1 <= tx:
                    if lis[ty][tx - 1] not in ["S","O"]:
                        tx -= 1
                    elif lis[ty][tx - 1] == "S":
                        return False
                    else:
                        break
    return True


ans = False
def backtrack(y, x, count):
    global ans
    if ans:
        return
    for i in range(y, n):
        for j in range(n):
            if count == 0 and check():
                ans = True
                return
            elif lis[i][j] == "X" and count > 0:
                lis[i][j] = "O"
                backtrack(i, j, count - 1)
                lis[i][j] = "X"


backtrack(0, 0, 3)
if ans:
    print("YES")
else:
    print("NO")
