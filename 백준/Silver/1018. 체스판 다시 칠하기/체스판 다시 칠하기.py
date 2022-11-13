n, m = map(int, input().split())
wtob = 0
btow = 0
lis = []
for i in range(n):
    t = input().split()
    lis.append(t)

# i는 가로 j는 세로 가로가 바뀔대마다 리스트 리셋
inans = 10000000000000
for i in range(0,m - 7):
    for j in range(0,n - 7):
        newlis = []
        for h in range(0,8):
            newlis.append(lis[h + j][0][i:i+8])
        # 이 지점에서 모든 경우의수가 다 저장이됨
        ans1 = 0
        ans2 = 0
        for a in range(8):
            if a % 2 == 0:
                for q in (0,2,4,6):
                    if newlis[a][q] == "W":
                        ans1 = ans1 + 1
                for p in (1,3,5,7):
                    if newlis[a][p] == "B":
                        ans1 = ans1 + 1
            elif a % 2 == 1:
                for q in (1,3,5,7):
                    if newlis[a][q] == "W":
                        ans1 = ans1 + 1
                for p in (0,2,4,6):
                    if newlis[a][p] == "B":
                        ans1 = ans1 + 1
        for a in range(8):
            if a % 2 == 0:
                for q in (0,2,4,6):
                    if newlis[a][q] == "B":
                        ans2 = ans2 + 1
                for p in (1,3,5,7):
                    if newlis[a][p] == "W":
                        ans2 = ans2 + 1
            elif a % 2 == 1:
                for q in (1,3,5,7):
                    if newlis[a][q] == "B":
                        ans2 = ans2 + 1
                for p in (0,2,4,6):
                    if newlis[a][p] == "W":
                        ans2 = ans2 + 1
        ans = 0
        if ans1 <= ans2:
            ans = ans1
        else:
            ans = ans2

        if ans < inans:
            inans = ans

print(inans)