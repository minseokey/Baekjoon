import sys

def coin(now):
    ans = 0
    while now > 0:
        tt = c.pop()
        ans += (now // tt)
        now %= tt
    return ans

minimum = float('inf')
n,k = map(int,sys.stdin.readline().split())
c = [int(sys.stdin.readline()) for _ in range(n)]
print(coin(k))
