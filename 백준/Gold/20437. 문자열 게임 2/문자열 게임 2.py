import sys

fois = int(sys.stdin.readline())
for _ in range(fois):
    string = list(sys.stdin.readline().strip())
    k = int(sys.stdin.readline())
    dic = dict()
    sus = set()
    for i, num in enumerate(string):
        if num in dic:
            dic[num][0] += 1
            dic[num][1].append(i)
            if dic[num][0] >= k:
                sus.add(num)

        else:
            dic[num] = [1, [i]]
            if dic[num][0] >= k:
                sus.add(num)

    if not sus:
        print(-1)
    else:
        maxx,minn = -100,100000
        for i in sus:
            t = dic[i][1]
            for j in range(k-1, len(t)):
                length = t[j] - t[j-(k-1)] + 1
                if length >= maxx:
                    maxx = length
                if length <= minn:
                    minn = length
        print(minn,maxx)