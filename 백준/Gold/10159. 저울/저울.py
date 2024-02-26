import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

pool_h = dict()
pool_l = dict()
for i in range(m):
    heavy,light = map(int,sys.stdin.readline().split())
    heavy -= 1
    light -= 1
    if heavy in pool_h.keys():
        pool_h[heavy].append(light)
    else:
        pool_h[heavy] = [light]

    if light in pool_l.keys():
        pool_l[light].append(heavy)
    else:
        pool_l[light] = [heavy]

for i in range(n):
    visited_h = [False] * n
    visited_h[i] = True
    stack = [i]
    while stack:
        t = stack.pop()
        if t in pool_h.keys():
            for j in pool_h[t]:
                if not visited_h[j]:
                    visited_h[j] = True
                    stack.append(j)

    visited_l = [False] * n
    visited_l[i] = True
    stack = [i]
    while stack:
        t = stack.pop()
        if t in pool_l.keys():
            for j in pool_l[t]:
                if not visited_l[j]:
                    visited_l[j] = True
                    stack.append(j)
    count = 0
    for j in range(n):
        if not visited_l[j] and not visited_h[j]:
            count += 1

    print(count)

