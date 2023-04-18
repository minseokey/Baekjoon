import itertools
import sys

al,lenn = map(int,sys.stdin.readline().split())
lis = list(map(int,sys.stdin.readline().split()))

ans = []
for i in itertools.combinations_with_replacement(lis, lenn):
    if sorted(i) not in ans:
        ans.append(sorted(i))


for i in sorted(ans):
    print(*i)