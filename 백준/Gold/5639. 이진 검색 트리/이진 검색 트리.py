import sys

sys.setrecursionlimit(10 ** 9)

def cut(start,end):
    if start > end:
        return
    else:
        root = lis[start]
        mid = end + 1
        for i in range(start+1, end+1):
            if lis[i] > root:
                mid = i
                break

        cut(start + 1,mid-1)
        cut(mid, end)
        print(root)


lis = []
while True:
    try:
        lis.append(int(sys.stdin.readline()))
    except:
        break

cut(0,len(lis) - 1)