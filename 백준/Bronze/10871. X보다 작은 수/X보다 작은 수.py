n, s = map(int,input().split())
l = list(map(int,input().split()))
for i in l:
    if i < s:
        print(i, end=" ")