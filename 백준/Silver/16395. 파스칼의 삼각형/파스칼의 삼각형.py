import sys

def pascal(n,k):
    if ptable[n][k] == -1:
        if k == 0 or k == n:
            ptable[n][k] = 1
            return 1
        else:
            ptable[n][k] = pascal(n-1,k-1) + pascal(n-1,k)
            return ptable[n][k]
    else:
        return ptable[n][k]

n,k = map(int,sys.stdin.readline().split())
ptable = [[-1] * 30 for _ in range(30)]
print(pascal(n-1,k-1))