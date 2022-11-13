n = input()
nint = int(n)
keylis = []

# (자리수 +1)*변수 를 다 더하면 n 이 나오는 각각의 변수들의 정수형 합
if len(n) == 1:
    if nint%2 != 0:
        print(0)
    else:
        print(nint // 2)
else:
    for i in range(nint - len(n)*10, nint):
        t = 0
        minilis = []
        a = i
        for j in range(1, len(str(i)) + 1):
            t = t + ((a // (10**(j-1))) % 10)
            minilis.append(((a // (10**(j-1))) % 10))
        if nint == i + t:
            q = 0
            for i in range(len(minilis)-1,-1,-1):
                q = q + minilis [i] * 10**(i)
            keylis.append(q)
    if len(keylis) >= 1:
        print(min(keylis))
    else:
        print(0)
