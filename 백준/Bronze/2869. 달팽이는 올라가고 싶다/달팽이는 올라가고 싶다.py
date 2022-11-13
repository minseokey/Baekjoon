import math
up,down,hight = map(int,input().split())
ans = ((hight - up)/(up - down) + 1)
print(math.ceil(ans))