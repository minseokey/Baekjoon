import sys

n = int(sys.stdin.readline())
lis = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 1개일 경우 예외처리
if n == 1:
    if lis[0][0] == 0:
        print(1)
    else:
        print(0)
else:
    # 두 개씩 묶어보자
    lis1 = []
    lis2 = []

    for i in range(n):
        for j in range(n):
            lis1.append(lis[i][0] + lis[j][1])
            lis2.append(-(lis[i][2] + lis[j][3]))

    lis1.sort()
    lis2.sort()

    # 투 포인터를 이용하여 합이 0이 되는 경우를 찾자.
    count = 0
    i, j = 0, 0
    len1, len2 = len(lis1), len(lis2)

    while i < len1 and j < len2:
        if lis1[i] < lis2[j]:
            i += 1
        elif lis1[i] > lis2[j]:
            j += 1
        else:
            # 동일한 값을 가진 요소들을 모두 센다.
            val1 = lis1[i]
            val2 = lis2[j]
            count1 = 0
            count2 = 0

            while i < len1 and lis1[i] == val1:
                count1 += 1
                i += 1

            while j < len2 and lis2[j] == val2:
                count2 += 1
                j += 1

            count += count1 * count2

    print(count)
