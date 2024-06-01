import sys

n = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))
dic = dict()
for now, head in enumerate(lis):
    if head == -1:
        dic[0] = []
    elif head in dic.keys():
        dic[head].append(now)
    else:
        dic[head] = [now]

if n > 1:
    dp = [0 for _ in range(n)]
    keylis = list(dic.keys())
    keylis.sort(reverse=True)

    for i in keylis:
        temp = []
        for j in dic[i]:
            temp.append(dp[j])
        temp.sort(reverse=True)
        for j in range(len(temp)):
            temp[j] += (j+1)
        dp[i] = max(temp)

    print(max(dp))
else:
    print(0)