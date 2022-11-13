import sys
n = int(input())

lis = []
for i in range(n):
    a = (sys.stdin.readline().strip())
    if (len(a),a) not in lis:
        lis.append((len(a),a))


lis.sort()
for i in lis:
    print(i[1])