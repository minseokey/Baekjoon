ans = int(input())
n = int(input())


for i in range(n):
    p,a = map(int,input().split())
    ans -= p*a

if ans == 0:
    print("Yes")
else:
    print("No")