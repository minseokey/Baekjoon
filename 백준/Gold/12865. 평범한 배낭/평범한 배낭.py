n, k = map(int, input().split())  # 물건의 수 n과 배낭의 용량 k 입력 받기

w = [0]  # 물건의 무게를 저장할 리스트
v = [0]  # 물건의 가치를 저장할 리스트

for i in range(n):
    a, b = map(int, input().split())  # 각 물건의 무게와 가치 입력 받기
    w.append(a)
    v.append(b)

# 2차원 배열 dp 생성하기
dp = [[0] * (k+1) for _ in range(n+1)]

# dp 배열 채우기
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]

# 배낭에 넣을 수 있는 물건들의 가치 합의 최댓값 출력하기
print(dp[n][k])
