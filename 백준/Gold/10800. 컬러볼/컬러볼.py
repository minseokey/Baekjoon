# 크기작고 색다른
import heapq
import sys

n = int(sys.stdin.readline())

lis = []
ordered_list = [0] * n
color_dict = {}
for i in range(n):
    co, si = map(int, sys.stdin.readline().split())
    heapq.heappush(lis, (si, co, i))

allsum = 0
last_ans = [-1,[-1]]
while lis:
    nsi, nco, order = heapq.heappop(lis)

    temp = allsum

    if nco in color_dict.keys():
        temp -= color_dict[nco]

    if nsi == last_ans[0]:
        for i in last_ans[1]:
            if i != nco:
                temp -= last_ans[0]
        last_ans[1].append(nco)
    else:
        last_ans = [nsi, [nco]]

    ordered_list[order] = temp
    if nco in color_dict.keys():
        color_dict[nco] += nsi
    else:
        color_dict[nco] = nsi

    allsum += nsi

for i in ordered_list:
    print(i)
