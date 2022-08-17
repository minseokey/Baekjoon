import sys
leng,ques = map(int,sys.stdin.readline().split())
lis = []
for i in range(leng):
    lis.append(sys.stdin.readline().strip())

for i in range(ques):
    inp = sys.stdin.readline()
    if 48 <= ord(inp[0]) <=57:
        print(lis[int(inp)-1])
    else:
        print(lis.index(inp.strip())+1)