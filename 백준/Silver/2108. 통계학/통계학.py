import sys, collections

n = int(sys.stdin.readline())
lis = []
w = 0
t = 0
wor = [0, 0]

for i in range(n):
    q = int(sys.stdin.readline())
    lis.append(q)
    w = w + q

kk = sorted(lis)

# 산술평균
print(int(round(w / n, 0)))

# 중앙값
print(kk[len(kk) // 2])

# 최빈값 얘가 문제인뎅..
kkcount = collections.Counter(kk)
if len(kkcount) == 1:
    print(kk[0])
else:
    if kkcount.most_common(2)[0][1] == kkcount.most_common(2)[1][1]:
        print(kkcount.most_common(2)[1][0])
    else:
        print(kkcount.most_common(2)[0][0])

# 범위
print(kk[n - 1] - kk[0])
