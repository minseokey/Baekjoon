import bisect
import sys

n = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))
lis.sort()
ans = 0

for pos, i in enumerate(lis):
    lis.remove(i)
    try:
        start = 0
        end = len(lis) - 1
        while end > start:
            if lis[start] + lis[end] > i:
                end -= 1
            elif lis[start] + lis[end] < i:
                start += 1
            else:
                ans += 1
                break
    except:
        pass
    lis.insert(pos,i)
print(ans)