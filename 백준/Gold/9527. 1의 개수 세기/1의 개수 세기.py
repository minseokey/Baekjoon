import sys

a,b = map(int,sys.stdin.readline().split())

# a 1개수 - b+1 1개
# 식은 ㅁ = 2 * a + 2 ** i
dp = [0]
for i in range(1,55):
    dp.append(2*dp[i-1] + 2**(i - 1))

def target(tar):
    num = 0
    origin = bin(tar)[2:]
    length = len(origin)
    for i in range(length):
        if origin[i] == '1':
            p = length-i-1
            num += dp[p]
            num += tar - 2**p + 1
            tar -= 2**p
    return num

print(target(b) - target(a-1))