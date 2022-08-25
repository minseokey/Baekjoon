import sys
com = int(sys.stdin.readline())
mapping = int(sys.stdin.readline())

checker = [x for x in range(1,com+1)]
dic = dict()
for i in range(mapping):
    ts,te = map(int,sys.stdin.readline().split())
    if ts not in dic.keys():
        dic[ts] = [te]
    else:
        dic[ts].append(te)
    if te not in dic.keys():
        dic[te] = [ts]
    else:
        dic[te].append(ts)


def recur(checker,mom):
    checker.remove(mom)
    if mom in dic.keys():
        for i in dic[mom]:
            if i in checker:
                recur(checker,i)

    else:
        return
recur(checker,1)
print(com - len(checker) - 1)