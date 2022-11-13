import sys
n = int(sys.stdin.readline())
numlis = list(map(int,sys.stdin.readline().split()))

summ = 0
line = len(numlis)
for i in sorted(numlis):
    summ += line*i
    line -= 1

print(summ)
