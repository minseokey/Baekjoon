n = int(input())
a = True
i = 0
k = 0
while a:
    i = i + 1
    if "666" in str(i):
        k = k + 1
    if k == n:
        a = False

print(i)