import sys


def rota(where, di):
    if di:  # 시계
        for _ in range(2):
            temp = cube[where][0][2]
            cube[where][0][2] = cube[where][0][1]
            cube[where][0][1] = cube[where][0][0]
            cube[where][0][0] = cube[where][1][0]
            cube[where][1][0] = cube[where][2][0]
            cube[where][2][0] = cube[where][2][1]
            cube[where][2][1] = cube[where][2][2]
            cube[where][2][2] = cube[where][1][2]
            cube[where][1][2] = temp
    else:  # 반시계
        for _ in range(2):
            temp = cube[where][0][0]
            cube[where][0][0] = cube[where][0][1]
            cube[where][0][1] = cube[where][0][2]
            cube[where][0][2] = cube[where][1][2]
            cube[where][1][2] = cube[where][2][2]
            cube[where][2][2] = cube[where][2][1]
            cube[where][2][1] = cube[where][2][0]
            cube[where][2][0] = cube[where][1][0]
            cube[where][1][0] = temp


# 1. 나 자신 돌아가기 -> rota , 2. 옆면끼리 교환.
def L(dir):
    # U4 <- F1 <- D5 <- B3 <- U4
    if dir == "-":
        for _ in range(3):
            temp = cube[5][0][0]
            cube[5][0][0] = cube[5][1][0]
            cube[5][1][0] = cube[5][2][0]
            cube[5][2][0] = cube[3][2][2]
            cube[3][2][2] = cube[3][1][2]
            cube[3][1][2] = cube[3][0][2]
            cube[3][0][2] = cube[4][0][0]
            cube[4][0][0] = cube[4][1][0]
            cube[4][1][0] = cube[4][2][0]
            cube[4][2][0] = cube[1][0][0]
            cube[1][0][0] = cube[1][1][0]
            cube[1][1][0] = cube[1][2][0]
            cube[1][2][0] = temp
        rota(0, False)
    # U4 -> F1 -> D5 -> B3 -> U4
    else:
        for _ in range(3):
            temp = cube[5][2][0]
            cube[5][2][0] = cube[5][1][0]
            cube[5][1][0] = cube[5][0][0]
            cube[5][0][0] = cube[1][2][0]
            cube[1][2][0] = cube[1][1][0]
            cube[1][1][0] = cube[1][0][0]
            cube[1][0][0] = cube[4][2][0]
            cube[4][2][0] = cube[4][1][0]
            cube[4][1][0] = cube[4][0][0]
            cube[4][0][0] = cube[3][0][2]
            cube[3][0][2] = cube[3][1][2]
            cube[3][1][2] = cube[3][2][2]
            cube[3][2][2] = temp
        rota(0, True)


def F(dir):
    # U4 <- R2 <- D5 <- L0 <- U4
    if dir == "-":
        for _ in range(3):
            temp = cube[5][0][2]
            cube[5][0][2] = cube[5][0][1]
            cube[5][0][1] = cube[5][0][0]
            cube[5][0][0] = cube[0][2][2]
            cube[0][2][2] = cube[0][1][2]
            cube[0][1][2] = cube[0][0][2]
            cube[0][0][2] = cube[4][2][0]
            cube[4][2][0] = cube[4][2][1]
            cube[4][2][1] = cube[4][2][2]
            cube[4][2][2] = cube[2][0][0]
            cube[2][0][0] = cube[2][1][0]
            cube[2][1][0] = cube[2][2][0]
            cube[2][2][0] = temp
        rota(1, False)
    # U4 -> R2 -> D5 -> L0 -> U4
    else:
        for _ in range(3):
            temp = cube[5][0][0]
            cube[5][0][0] = cube[5][0][1]
            cube[5][0][1] = cube[5][0][2]
            cube[5][0][2] = cube[2][2][0]
            cube[2][2][0] = cube[2][1][0]
            cube[2][1][0] = cube[2][0][0]
            cube[2][0][0] = cube[4][2][2]
            cube[4][2][2] = cube[4][2][1]
            cube[4][2][1] = cube[4][2][0]
            cube[4][2][0] = cube[0][0][2]
            cube[0][0][2] = cube[0][1][2]
            cube[0][1][2] = cube[0][2][2]
            cube[0][2][2] = temp
        rota(1, True)


def R(dir):
    # U4 <- B3 <- D5 <- F1 <- U4
    if dir == "-":
        for _ in range(3):
            temp = cube[5][2][2]
            cube[5][2][2] = cube[5][1][2]
            cube[5][1][2] = cube[5][0][2]
            cube[5][0][2] = cube[1][2][2]
            cube[1][2][2] = cube[1][1][2]
            cube[1][1][2] = cube[1][0][2]
            cube[1][0][2] = cube[4][2][2]
            cube[4][2][2] = cube[4][1][2]
            cube[4][1][2] = cube[4][0][2]
            cube[4][0][2] = cube[3][0][0]
            cube[3][0][0] = cube[3][1][0]
            cube[3][1][0] = cube[3][2][0]
            cube[3][2][0] = temp
        rota(2, False)
    # U4 -> B3 -> D5 -> F1 -> U4
    else:
        for _ in range(3):
            temp = cube[5][0][2]
            cube[5][0][2] = cube[5][1][2]
            cube[5][1][2] = cube[5][2][2]
            cube[5][2][2] = cube[3][2][0]
            cube[3][2][0] = cube[3][1][0]
            cube[3][1][0] = cube[3][0][0]
            cube[3][0][0] = cube[4][0][2]
            cube[4][0][2] = cube[4][1][2]
            cube[4][1][2] = cube[4][2][2]
            cube[4][2][2] = cube[1][0][2]
            cube[1][0][2] = cube[1][1][2]
            cube[1][1][2] = cube[1][2][2]
            cube[1][2][2] = temp
        rota(2, True)


def B(dir):
    # U4 <- R2 <- D5 <- L0 <- U4
    if dir == "-":
        for _ in range(3):
            temp = cube[5][2][0]
            cube[5][2][0] = cube[5][2][1]
            cube[5][2][1] = cube[5][2][2]
            cube[5][2][2] = cube[2][2][2]
            cube[2][2][2] = cube[2][1][2]
            cube[2][1][2] = cube[2][0][2]
            cube[2][0][2] = cube[4][0][2]
            cube[4][0][2] = cube[4][0][1]
            cube[4][0][1] = cube[4][0][0]
            cube[4][0][0] = cube[0][0][0]
            cube[0][0][0] = cube[0][1][0]
            cube[0][1][0] = cube[0][2][0]
            cube[0][2][0] = temp
        rota(3, False)
    # U -> R -> D -> L <- U
    else:
        for _ in range(3):
            temp = cube[5][2][2]
            cube[5][2][2] = cube[5][2][1]
            cube[5][2][1] = cube[5][2][0]
            cube[5][2][0] = cube[0][2][0]
            cube[0][2][0] = cube[0][1][0]
            cube[0][1][0] = cube[0][0][0]
            cube[0][0][0] = cube[4][0][0]
            cube[4][0][0] = cube[4][0][1]
            cube[4][0][1] = cube[4][0][2]
            cube[4][0][2] = cube[2][0][2]
            cube[2][0][2] = cube[2][1][2]
            cube[2][1][2] = cube[2][2][2]
            cube[2][2][2] = temp
        rota(3, True)


def U(dir):
    # L0 <- B3 <- R2 <- F1 <- L0
    if dir == "-":
        for _ in range(3):
            temp = cube[1][0][2]
            cube[1][0][2] = cube[1][0][1]
            cube[1][0][1] = cube[1][0][0]
            cube[1][0][0] = cube[0][0][2]
            cube[0][0][2] = cube[0][0][1]
            cube[0][0][1] = cube[0][0][0]
            cube[0][0][0] = cube[3][0][2]
            cube[3][0][2] = cube[3][0][1]
            cube[3][0][1] = cube[3][0][0]
            cube[3][0][0] = cube[2][0][2]
            cube[2][0][2] = cube[2][0][1]
            cube[2][0][1] = cube[2][0][0]
            cube[2][0][0] = temp
        rota(4, False)
    # L0 -> B3 -> R2 -> F1 -> L0
    else:
        for _ in range(3):
            temp = cube[1][0][0]
            cube[1][0][0] = cube[1][0][1]
            cube[1][0][1] = cube[1][0][2]
            cube[1][0][2] = cube[2][0][0]
            cube[2][0][0] = cube[2][0][1]
            cube[2][0][1] = cube[2][0][2]
            cube[2][0][2] = cube[3][0][0]
            cube[3][0][0] = cube[3][0][1]
            cube[3][0][1] = cube[3][0][2]
            cube[3][0][2] = cube[0][0][0]
            cube[0][0][0] = cube[0][0][1]
            cube[0][0][1] = cube[0][0][2]
            cube[0][0][2] = temp
        rota(4, True)


def D(dir):
    # L0 <- F1 <- R2 <- B3 <- L0
    if dir == "-":
        for _ in range(3):
            temp = cube[3][2][0]
            cube[3][2][0] = cube[3][2][1]
            cube[3][2][1] = cube[3][2][2]
            cube[3][2][2] = cube[0][2][0]
            cube[0][2][0] = cube[0][2][1]
            cube[0][2][1] = cube[0][2][2]
            cube[0][2][2] = cube[1][2][0]
            cube[1][2][0] = cube[1][2][1]
            cube[1][2][1] = cube[1][2][2]
            cube[1][2][2] = cube[2][2][0]
            cube[2][2][0] = cube[2][2][1]
            cube[2][2][1] = cube[2][2][2]
            cube[2][2][2] = temp
        rota(5, False)
    # L0 -> F1 -> R2 -> B3 -> L0
    else:
        for _ in range(3):
            temp = cube[3][2][2]
            cube[3][2][2] = cube[3][2][1]
            cube[3][2][1] = cube[3][2][0]
            cube[3][2][0] = cube[2][2][2]
            cube[2][2][2] = cube[2][2][1]
            cube[2][2][1] = cube[2][2][0]
            cube[2][2][0] = cube[1][2][2]
            cube[1][2][2] = cube[1][2][1]
            cube[1][2][1] = cube[1][2][0]
            cube[1][2][0] = cube[0][2][2]
            cube[0][2][2] = cube[0][2][1]
            cube[0][2][1] = cube[0][2][0]
            cube[0][2][0] = temp
        rota(5, True)



fois = int(sys.stdin.readline())

for _ in range(fois):
    n = int(sys.stdin.readline())
    lis = list(sys.stdin.readline().split())
    '''
          (4,U)
    (0,L) (1,F) (2,R) (3,B)  이렇게 이루어져있다고 가정하자.
          (5,D)
          
    한번 돌릴때마다 4개씩 돌아간다. -> 돌리는 면 자체가 돌아가는것이당
    '''
    cube = [[["g", "g", "g"] for _ in range(3)], [["r", "r", "r"] for _ in range(3)],
            [["b", "b", "b"] for _ in range(3)],
            [["o", "o", "o"] for _ in range(3)], [["w", "w", "w"] for _ in range(3)],
            [["y", "y", "y"] for _ in range(3)]]



    for i in lis:
        if i[0] == "L":
            L(i[1])
        elif i[0] == "F":
            F(i[1])
        elif i[0] == "R":
            R(i[1])
        elif i[0] == "B":
            B(i[1])
        elif i[0] == "U":
            U(i[1])
        elif i[0] == "D":
            D(i[1])


    for i in cube[4]:
        print("".join(i))