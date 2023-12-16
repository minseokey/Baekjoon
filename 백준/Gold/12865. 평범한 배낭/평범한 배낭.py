import sys

n, k = map(int, sys.stdin.readline().split())
arr = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    size, value = map(int, sys.stdin.readline().split())
    for j in range(1, k + 1):
        if j - size >= 0:
            arr[i][j] = max(arr[i - 1][j], arr[i-1][j - size] + value)
        else:
            arr[i][j] = arr[i - 1][j]

print(arr[n][k])