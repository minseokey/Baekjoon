import sys
n,m = map(int,sys.stdin.readline().split())

coin = [0] * n
for i in range(n):
    coin[i]=(int(sys.stdin.readline()))
num = 0

for i in reversed(coin):
    num += int(m/i)
    m %= i
    if m == 0:
        break
print(num)