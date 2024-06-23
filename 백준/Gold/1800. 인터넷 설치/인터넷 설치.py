import heapq
import sys

n, p, k = map(int, sys.stdin.readline().split())

dic = dict()
costlis = []
for i in range(1, n + 1):
    dic[i] = []
for i in range(p):
    s, e, w = map(int, sys.stdin.readline().split())
    dic[s].append((e, w))
    dic[e].append((s, w))
    costlis.append(w)


# 가격이 cost 일때, 사용한 쿠폰의 개수를 저장하자.
def dijk(cost):
    weight = [float('inf') for _ in range(n + 1)]
    weight[1] = 0
    queue = [[0, 1]]  # 몇개의 쿠폰을 사용했는지, 현재의 노드.

    while queue:
        coupon, now = heapq.heappop(queue)
        if weight[now] >= coupon:
            for next_node, next_cost in dic[now]:
                if cost < next_cost:
                    if weight[next_node] > coupon + 1:
                        weight[next_node] = coupon + 1
                        heapq.heappush(queue, [coupon + 1, next_node])
                else:
                    if weight[next_node] > coupon:
                        weight[next_node] = coupon
                        heapq.heappush(queue, [coupon, next_node])
    return weight[-1]


costlis.sort()
start, end = 0, len(costlis) - 1

answer = -1
while end >= start:
    mid = (start + end) // 2
    now_k = dijk(costlis[mid])
    if now_k > k:
        start = mid + 1
    elif now_k <= k:
        if mid == 0:
            answer = -2
        else:
            answer = mid
        end = mid - 1

if answer == -2:
    print(0)
elif answer == -1:
    print(-1)
else:
    print(costlis[answer])
