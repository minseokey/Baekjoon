import sys
leng,ques = map(int,sys.stdin.readline().split())
lis ={}
for i in range(leng):
    lis[sys.stdin.readline().strip()] = i
kkk = list(lis)
for i in range(ques):
    inp = sys.stdin.readline()
    if 48 <= ord(inp[0]) <=57:
        print(kkk[int(inp) -1])
    else:
        print(lis[inp.strip()]+1)