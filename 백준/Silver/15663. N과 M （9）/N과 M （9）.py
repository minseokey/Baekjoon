import itertools
import sys

n,m = map(int,sys.stdin.readline().split())
k = sorted(list(map(int,sys.stdin.readline().split())))
for i in sorted(list(set((itertools.permutations(k,m))))):
    print(*i)
