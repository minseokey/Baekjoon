import sys

n, k = map(int, sys.stdin.readline().split())
convey = []
temp = list(map(int, sys.stdin.readline().split()))
convey.append(temp[:n])
convey.append(temp[n:][::-1])

nowlis = [False for _ in range(n)]

count = 0

while True:
    count += 1

    # 1. 벨트가 회전
    nowlis.pop()
    nowlis.insert(0, False)
    nowlis[-1] = False

    convfir = convey[0].pop()
    convsec = convey[1].pop(0)
    convey[0].insert(0, convsec)
    convey[1].append(convfir)



    # 2. 벨트위에서 전진 (먼저 올라간 애 부터)
    for i in range(n - 2, 0, -1):
        if nowlis[i] and not nowlis[i + 1] and convey[0][i + 1] > 0:
            nowlis[i] = False
            nowlis[i+1] = True
            convey[0][i+1] -= 1
        nowlis[n-1] = False

    # 3. 올리는 칸의 내구도가 0이 아니면 새 로봇 올리기
    if convey[0][0] > 0 and not nowlis[0]:
        convey[0][0] -= 1
        nowlis[0] = True

    # 4. 내구도 0인 칸이 k 개 이상? -> 종료
    if convey[0].count(0) + convey[1].count(0) >= k:
        break

print(count)
