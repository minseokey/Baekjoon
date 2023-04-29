import sys

n = int(sys.stdin.readline())

lis = list(map(int,sys.stdin.readline().split()))
lisreverse = list(reversed(lis))

# 서브시퀀스 길이
def subsequence(lis):
    lisalready = [1 for i in range(len(lis))]
    for i in range(len(lis)):
        nownode = 0
        for j in range(0, i):
            if lis[j] < lis[i]:
                nownode = max(nownode, lisalready[j])
        lisalready[i] = nownode + 1

    return lisalready


ll = subsequence(lis)
rll = list(reversed(subsequence(lisreverse)))

ans = 1
for i in range(n-1):
    ans = max(ans, ll[i] + rll[i] - 1)

print(ans)
