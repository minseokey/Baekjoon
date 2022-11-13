n = int(input())
lis = []
ans = 0
for i in range(n):
    lis.append(list(map(int,input().split())))  # 현재 2중 리스트

def qqq(col):
    lis[col+1][0] = min(lis[col][1] + lis[col + 1][0],lis[col][2] + lis[col+1][0])

    lis[col+1][1] = min(lis[col][0] + lis[col+1][1],lis[col][2] + lis[col + 1][1])

    lis[col+1][2] = min(lis[col][0] + lis[col + 1][2],lis[col][1] + lis[col+1][2])






for i in range(n - 1):
    qqq(i)

print(min(lis[n-1]))