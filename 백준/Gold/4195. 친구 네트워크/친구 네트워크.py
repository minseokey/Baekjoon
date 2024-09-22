import sys

n = int(sys.stdin.readline())


def find(a):
    if up[a] != a:
        up[a] = find(up[a])
    return up[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        up[b] = a
        size[a] += size[b]

    print(size[a])


for _ in range(n):
    friend = dict()
    up = []
    size = []
    q = int(sys.stdin.readline())
    for _ in range(q):

        # 사용자 추가
        a, b = sys.stdin.readline().split()
        if a not in friend:
            friend[a] = len(friend.keys())
            up.append(friend[a])
            size.append(1)
        if b not in friend:
            friend[b] = len(friend.keys())
            up.append(friend[b])
            size.append(1)

        # 네트워크 합치기
        union(friend[a], friend[b])

