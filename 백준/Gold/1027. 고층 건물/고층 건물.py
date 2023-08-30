import sys

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))

anslis = [0 for i in range(n)]

for i in range(len(lis)):
    # i를 기준으로 양 옆에 볼 수 있는 고층빌딩 개수 카운트-> 기울기 갱신
    # left
    left = lis[:i]
    # right
    right = lis[i + 1:]
    # now
    now = lis[i]

    gradleft = -float("inf")
    for j in range(len(left) - 1, -1, -1):
        nowgrad = (left[j] - now) / (len(left) - j)
        if nowgrad > gradleft:
            gradleft = nowgrad
            anslis[i] += 1

    gradright = -float("inf")
    for j in range(len(right)):
        nowgrad = (right[j] - now) / (j + 1)
        if nowgrad > gradright:
            gradright = nowgrad
            anslis[i] += 1

print(max(anslis))