x, y, w, h = map(int,input().split())
lis = [w - x, h - y, x, y]
print(min(lis))