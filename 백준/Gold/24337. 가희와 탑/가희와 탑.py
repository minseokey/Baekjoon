import sys

n,a,b = map(int,sys.stdin.readline().split())

# 1. 최고높이는 무엇인가. -> a
# 2. 최고높이 기준으로 최소 a:b 하지만 111123421 처럼 되어야 최소 (9,4,3)
# 3. 조건을 만족하지 않는 조건 -> a+b-2 > n 일때 만족 12341 = (5,4,2) -> O (4,4,2) -> X

if a+b-2 >= n:
    print(-1)
elif a != 1:
    ans = []
    if b > a:
        for i in range(1,a):
            ans.append(str(i))
        for i in range(b,0,-1):
            ans.append(str(i))
        ans = ["1"] * (n - len(ans)) + ans
        print(" ".join(ans))
    else:
        for i in range(1, a+1):
            ans.append(str(i))
        for i in range(b-1, 0, -1):
            ans.append(str(i))
        ans = ["1"] * (n - len(ans)) + ans
        print(" ".join(ans))
else:
    ans = []

    for i in range(1, a + 1):
        ans.append(str(i))
    ans[-1] = str(b)
    ans += ["1"] * (n - (a + b - 1))
    for i in range(b - 1, 0, -1):
        ans.append(str(i))

    print(" ".join(ans))