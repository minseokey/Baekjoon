import sys

n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))

# dp 구조를 어캐 만들어야 할까?
# index => 중간점, 내용물 => 중간점 기준 어디까지 펠린드롬인가
dp = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    dp[i][i] = True

def pel(start, end):
    mid = ((end - start) // 2) + start

    # 짝수, 가운데 두개부터 시작
    if (end - start) % 2 == 1:
        midstart = mid
        midend = mid + 1

    # 홀수, 맨 가운데 제외 양쪽부터 시작.
    else:
        midstart = mid - 1
        midend = mid + 1

    ms, me = midstart, midend
    breakey = False
    while midstart >= start and midend <= end:
        if dp[midstart][midend]:
            break
        elif lis[midstart] == lis[midend]:
            midstart -= 1
            midend += 1
        else:
            breakey = True
            break

    if not breakey:
        while ms > start and me < end:
            if dp[ms][me]:
                break
            else:
                dp[ms][me] = True
                ms -= 1
                me += 1

    return breakey


for i in range(int(sys.stdin.readline())):
    start, end = map(int, sys.stdin.readline().split())
    if start == end:
        print(1)
    elif not pel(start - 1, end - 1):
        print(1)
    else:
        print(0)
