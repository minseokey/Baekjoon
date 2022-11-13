import sys,itertools
a,b = map(int,sys.stdin.readline().strip().split())
lis = [i for i in range(1,a + 1)]

kk = list(itertools.combinations_with_replacement(lis,b))


for j in kk:
    print(" ".join(str(j[i]) for i in range(b)))