import sys

n = int(sys.stdin.readline())
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lis.sort()

mind = max(lis, key=lambda x: x[1])[0]
ans = max(lis, key=lambda x:x[1])[1]
f_max = 0
f_count = 0
for i in range(min(lis)[0], mind):
    if i == lis[f_count][0]:
        if lis[f_count][1] > f_max:
            f_max = lis[f_count][1]
        f_count += 1
    ans += f_max

r_max = 0
r_count = len(lis)-1
for i in range(max(lis)[0], mind, -1):
    if i == lis[r_count][0]:
        if lis[r_count][1] > r_max:
            r_max = lis[r_count][1]
        r_count -= 1
    ans += r_max

print(ans)