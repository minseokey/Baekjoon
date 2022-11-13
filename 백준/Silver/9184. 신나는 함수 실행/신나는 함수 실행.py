import sys

p = True
lis = [[["_" for i in range(21)]for j in range(21)]for k in range(21)]




# 3중 리스트 각각의 자리를 비워놨어, 여길 채우는게 실력 ㅋ
# 각각의 수 a,b,c 를 이용하여 재귀 함수 형식으로 만들기

def Wmethod(x: int, y: int, z: int):
    global lis
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    elif x > 20 or y > 20 or z > 20:
        return 1048576

    if lis[x][y][z] != "_" :
        return lis[x][y][z]


    if x < y < z:
        lis[x][y][z] = Wmethod(x, y, z - 1) + Wmethod(x, y - 1, z - 1) - Wmethod(x, y - 1, z)
    else:
        lis[x][y][z] = Wmethod(x - 1, y, z) + Wmethod(x - 1, y - 1, z) + Wmethod(x - 1, y, z - 1) - Wmethod(x - 1,y - 1,z - 1)

    return lis[x][y][z]


    # 이 위까지는 자명
    # 이제부터 빠르게 구할 수 있는 방법을 생각해 보자


while p:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == -1 and b == -1 and c == -1:
        p = False
    else:
        print("w({}, {}, {}) = {}".format(a,b,c,Wmethod(a, b, c)))
