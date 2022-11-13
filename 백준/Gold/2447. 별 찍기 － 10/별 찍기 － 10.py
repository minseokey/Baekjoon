# 별찍기 마당 만들기 (공백 마당)
n = int(input())
lis = [["*"] * n for i in range(n)]


# 빈칸으로 이루어진 n*n 개의 이중 리스트 생성
# 무엇이 매개변수로 들어가면 좋을까?

# x = x좌표 시작점
# y = y좌표 시작점
# l = 빈칸 크기의 한변
# w = 한 빈칸과 다음 빈칸 까지의 간격
# t = 빈칸을 포함한 액자의 크기의 한변 3의 제곱수

def star(x, y, l, w, t):
    if x == 1:
        for i in range(1, n, 3):
            for j in range(1, n, 3):
                for k in range(0, 1):
                    for m in range(0, 1):
                        lis[i + k][j + m] = " "
        return lis

    else:
        for i in range(x, n, w):
            for j in range(y, n, w):
                for k in range(0, l):
                    for m in range(0, l):
                        lis[i + k][j + m] = " "
        return star(x // 3, y // 3, l // 3, w // 3, t // 3)


star(n // 3, n // 3, n // 3, n, n)
# 리스트 까지는 맞는다! 이제 리스트의 출력법만 만들자!
for i in range(n):
    print("".join(lis[i]))