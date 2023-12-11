import sys

n = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))

dp = [0] * (n+1)
dp[0] = lis[0]  # 초기값 설정

for i in range(n):  # 매 숫자를 돌며
    tempmax = 0
    for j in range(i):  # 이전의 숫자들에 대해 현재숫자보다 작은 수의 최대 합.
        if lis[i] > lis[j]:
            tempmax = max(tempmax, dp[j])
    dp[i] = tempmax + lis[i]

print(max(dp))