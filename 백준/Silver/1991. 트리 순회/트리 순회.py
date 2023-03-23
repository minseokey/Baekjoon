import sys

n = int(sys.stdin.readline())
lis = []
for i in range(n):
    lis.append(sys.stdin.readline().strip().split())

lispre = []
# 1 -> 2 -> 3
def preorder(node):
    for i in lis:
        if i[0] == node:
            lispre.append(i[0])
            preorder(i[1])
            preorder(i[2])

lispro = []
# 2 -> 1 -> 3
def proorder(node):
    for i in lis:
        if i[0] == node:
            proorder(i[1])
            proorder(i[2])
            lispro.append(i[0])

liscent = []
# 2 -> 3 -> 1
def centralorder(node):
    for i in lis:
        if i[0] == node:
            centralorder(i[1])
            liscent.append(i[0])
            centralorder(i[2])



preorder(lis[0][0])
centralorder(lis[0][0])
proorder(lis[0][0])

print("".join(lispre))
print("".join(liscent))
print("".join(lispro))
