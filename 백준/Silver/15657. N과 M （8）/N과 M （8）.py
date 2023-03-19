import itertools
import sys

N,M = map(int,sys.stdin.readline().split())
lis = list(map(int,sys.stdin.readline().split()))


temp = list(itertools.combinations_with_replacement(sorted(lis),M))

for i in range(len(temp)):
    print(*list(temp[i]))
