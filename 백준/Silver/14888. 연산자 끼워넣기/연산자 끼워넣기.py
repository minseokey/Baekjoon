import sys,itertools
n = int(sys.stdin.readline())
lis = list(sys.stdin.readline().strip().split())
pl,mi,mul,div = map(int,sys.stdin.readline().strip().split())
lisdiv = ["pl"] * pl + ["mi"] * mi + ["mul"] * mul + ["div"] * div
lisdiv = list(itertools.permutations(lisdiv))
ins = lis[0]
numlis = []
for j in range(len(lisdiv)):
    num = int(lis[0])
    for i in range(1,n):
        if lisdiv[j][i - 1] == "pl":
            num = num + int(lis[i])
        elif lisdiv[j][i - 1] == "mi":
            num = num - int(lis[i])
        elif lisdiv[j][i - 1] == "mul":
            num = num * int(lis[i])
        elif lisdiv[j][i - 1] == "div":
            if num < 0:
                num = -(abs(num) // int(lis[i]))
            else:
                num = num // int(lis[i])

    numlis.append(num)

print(max(numlis))
print(min(numlis))