import sys

def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])
            temp[i][j] %= 1000000
    return temp


def matrix_pow(k, M):
    if k == 1:
        return M
    if k % 2 == 0:
        temp = matrix_pow(k // 2, M)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(k - 1, M)
        return matrix_mult(temp, M)


A = [[1, 1], [1, 0]]
tmp = int(sys.stdin.readline().strip())
if tmp == 0:
    print(0)
elif tmp == 1:
    print(1)
else:
    print(matrix_pow(tmp - 1, A)[0][0])
