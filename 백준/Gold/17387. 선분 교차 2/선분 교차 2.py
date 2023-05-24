import sys

# 1번 점
Ax, Ay, Bx, By = map(int, sys.stdin.readline().split())
# 2번 점
Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())

A = [Ax, Ay]
B = [Bx, By]
C = [Cx, Cy]
D = [Dx, Dy]

line1 = [A, B]
line2 = [C, D]


# -1 => 반시계
# 1 => 시계
# 0 => 평행
def ccw(A, B, C):
    a1, a2 = A[0], A[1]
    b1, b2 = B[0], B[1]
    c1, c2 = C[0], C[1]

    sl = (a1 * b2 + b1 * c2 + c1 * a2) - (a2 * b1 + b2 * c1 + c2 * a1)
    if sl < 0:
        return -1
    elif sl > 0:
        return 1
    else:
        return 0


# 1번 라인 중심
ABC = ccw(A, B, C)
ABD = ccw(A, B, D)

# 2번 라인 중심
CDA = ccw(C, D, A)
CDB = ccw(C, D, B)

# 1번 선 AB, 2번 선  CD
if ABC * ABD == 0 and CDA * CDB == 0:
    # AB,CD 직선 비교 Max = B
    if A > B:
        temp = A
        A = B
        B = temp
    # Max = D
    if C > D:
        temp = C
        C = D
        D = temp
    if A <= D and C <= B:
        print(1)
    else:
        print(0)

elif ABC * ABD <= 0 and CDA * CDB <= 0:
    print(1)
else:
    print(0)
