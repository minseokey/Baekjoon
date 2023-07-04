import sys

lis = sys.stdin.readline().strip()
n = len(lis)
dplis = [[False for _ in range(n)] for _ in range(n)]
# dplis 에 각각 짝수일때 펠린드롬, 홀수일때 펠린드롬 각각 구하기
dp = [float('inf') for _ in range(n+1)]
dp[-1]=0

for i in range(n):


    # 우선 홀수
    st,en = i,i
    while st >= 0 and en < n:
        if lis[st] == lis[en]:
            dplis[st][en] = True
            st -= 1
            en += 1
        else:
            break

    # 짝수
    st,en = i-1,i
    while st >= 0 and en < n:
        if lis[st] == lis[en]:
            dplis[st][en] = True
            st -= 1
            en += 1
        else:
            break



for i in range(n):
    for j in range(1+i):
        if dplis[j][i]:
            dp[i] = min(dp[i],dp[j-1]+1)
        else:
            dp[i] = min(dp[i],dp[i-1]+1)

print(dp[n-1])
